import datetime
import json
import logging
import os
import posixpath
import tempfile
import types
from argparse import Namespace
from logging import Logger
from pathlib import Path
from typing import TextIO

import pandas as pd


class Snowflake:
    CCGI_BUCKET = 'district-sharing'
    MAX_DAYS = 7

    def __init__(self, args):
        self.log = self.init_log()
        self.fileList = self.get_file_list(args)

        self.CCGI = types.SimpleNamespace()  # ccgiUtilities.CCGIUtilities()
        self.s3 = types.SimpleNamespace()  # self.CCGI.create_ccgis3_conn()
        self.SFconn = types.SimpleNamespace()  # self.CCGI.create_snowflake_conn()

    @staticmethod
    def init_log() -> Logger:
        # create logger
        logger = logging.getLogger('Data_Reporting')
        logger.setLevel(logging.DEBUG)
        # create handler for logfile
        if not os.path.exists('Logs'):
            os.makedirs('Logs')
        log_name = os.path.join('Logs', 'Application_run_{:%Y%m%d}.log'.format(datetime.date.today()))
        fh = logging.FileHandler(log_name, mode='a')
        fh.setLevel(logging.DEBUG)
        # create handler for console stream
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # configure message formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add handlers to logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

    @staticmethod
    def get_last_saturday() -> datetime:
        d_now = datetime.date.today()
        d_idx = (d_now.weekday() + 1) % 7
        return d_now - datetime.timedelta(7 + d_idx - 6)

    @staticmethod
    def parse_sql_file(query_file: TextIO):
        metadata = ''
        line = query_file.readline()
        while line != '--\n':
            metadata += line
            line = query_file.readline()
            if not line:
                raise EOFError(f'improper metadata header: missing end sentinel in {query_file}')
        metadata = metadata.replace('/*', '').replace('*/', '')
        metadata_json = json.loads(metadata)
        query = query_file.read()
        return metadata_json, query

    @classmethod
    def make_name(cls, fname: str) -> str:
        return f'{Path(fname).stem}_data_{cls.get_last_saturday().strftime('%Y%m%d')}'

    def get_file_list(self, args: Namespace) -> list[str]:
        file_list = []
        if args.filePath:
            for file_path in args.filePath:
                if os.path.isdir(file_path):
                    file_list.extend([f"{Path(file_path).name}/{file}" for file in os.listdir(file_path) if
                                      file.endswith('.sql')])
                elif os.path.isfile(file_path):
                    file_list.append(f"{Path(file_path).parent.name}/{os.path.basename(file_path)}")
                else:
                    self.log.warning(f"File(s) path: {file_path} is not valid.")

        if not file_list:
            self.log.warning('No query files found using parameters given')

        return file_list

    def to_email(self, output_file, metadata: dict):
        attach = None
        body = 'The latest report for this query has been run.'
        if metadata['district']:
            body += "  The data has been uploaded to your district's SFTP folder"
        if metadata['attachData']:
            attach = output_file
            body += '\n\nA copy of the report is attached for your convenience.'
        if metadata["toGDrive"]:
            body += '\n\nThe data has been uploaded to the Internal Team Data Sharing folder on Google Drive.'

        self.CCGI.sendMsg(metadata['toNotify'],  # msg to
                          f'New data report: {output_file.name}',  # msg subject
                          body,  # msg text
                          attach)  # msg attachment

    def to_drive(self, output_file, report_type: str):
        drive_id = self.CCGI.drive_id
        folder_ids = self.CCGI.folder_id_dict
        drive = self.CCGI.gdrive()
        output_file.seek(0)
        folder_id = folder_ids.get(report_type,  # get destination folder from above based on report type
                                   self.CCGI.default_folder_id)  # if no type given for the file (or no match), default to parent folder

        self.clean_folder(drive, drive_id, folder_id)

        f = drive.CreateFile({
            'title': output_file.name,
            'parents': [{
                'kind': 'drive#fileLink',
                'teamDriveId': drive_id,
                'id': folder_id
            }]
        })
        f.SetContentString(output_file.read())

        f.Upload(param={'supportsTeamDrives': True})
        if report_type:
            self.log.info(f'uploaded file to {report_type} folder on shared drive')
        else:
            self.log.warning(f'Unknown or no report type "{report_type}" set for file {output_file.name}.  '
                             'File uploaded to Platform Data Sharing parent folder on shared drive.')

    def to_s3_temp(self, output_file, metadata: dict):
        output_file.seek(0)
        locations = {'plans': 'academic_plans',
                     'apps': 'applications',
                     'assessments': 'assessments',
                     'favorites': 'favorites',
                     'journals': 'journals',
                     'goals': 'goals',
                     'ag': 'a-g'}
        folder = locations.get(metadata['rType'], '')
        if not folder:
            self.log.warning(f'no recognized report folder for report type {metadata['rType']}, writing to district main folder')
        s3_folder_template = (posixpath.join(*['{district}', '{folder}', '{f}'])
                              .format(district=metadata['district'],
                                      folder=folder,
                                      f=output_file.name))
        s3_folder_template = posixpath.normpath(s3_folder_template)
        with open('{}'.format(output_file.name), mode='wb+') as outF:
            outF.write(output_file.read().encode('utf8'))
            outF.seek(0)
            self.s3.upload_fileobj(outF, self.CCGI_BUCKET, s3_folder_template)
        os.remove(f'{output_file.name}')

        self.log.info(f'{output_file.name} successfully uploaded to {self.CCGI_BUCKET}/{s3_folder_template}')

    def clean_folder(self, drive, drive_id, folder_id):
        def data_source_date(filename):
            return datetime.datetime.strptime(filename[:-4].split('_')[-1], '%Y%m%d').date()

        def get_files(folder_id, drive_id):
            return drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id),
                                   'corpora': "teamDrive",
                                   'teamDriveId': drive_id,
                                   'includeItemsFromAllDrives': True,
                                   'supportsAllDrives': True}).GetList()

        self.log.info('scanning for old files')
        ## recurse the directory for all files
        files = []
        folders = [folder_id]

        while folders:
            f_id = folders.pop()
            f_list = get_files(f_id, drive_id)
            for f_ in f_list:
                if f_['mimeType'] == 'application/vnd.google-apps.folder':
                    folders.append(f_['id'])
                else:
                    files.append(f_)

        ## This block should remove any files more than MAX_DAYS old in a report folder
        for f_ in files:
            if ((f_['title'].endswith('.csv')) and
                    (datetime.date.today() - data_source_date(f_['title'])).days > self.MAX_DAYS):
                try:
                    self.log.info(f'Sending {f_['title']} to trash: source data more than {self.MAX_DAYS} days old.')
                    f_.Trash(param={'supportsTeamDrives': True})
                except Exception as e:
                    self.log.warning(f'Error: {e}, could not send {f_['title']} to trash')

    def process_files(self):
        if self.fileList:
            for filename in self.fileList:
                report_name = os.path.basename(filename)
                try:
                    self.log.info(f'Now processing query: {filename}')
                    with open(f'./QueryFiles/{filename}', 'r') as inFile:
                        metadata, query = self.parse_sql_file(inFile)
                        if query:
                            df = pd.read_sql_query(query, self.SFconn)
                            if df.size > 0:
                                self.log.info(f'{filename} query successfully run and read to dataframe.')
                            else:
                                self.log.warning(f'{filename} query generated empty dataframe.')
                        else:
                            df = pd.DataFrame()

                    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', newline='') as output_file:
                        output_file.name = f'{self.make_name(report_name)}.csv'
                        df.to_csv(output_file, index=False)

                        if metadata['district']:
                            self.to_s3_temp(output_file, metadata)

                        if metadata['toNotify']:
                            self.to_email(output_file, metadata)
                            self.log.info(f'sent email notification to {metadata["toNotify"]}')
                        else:
                            self.log.warning('no email notification specified')

                        if metadata['toGDrive']:
                            self.to_drive(output_file, metadata['rType'])

                except Exception as e:
                    self.log.error(f'error encountered while running query {filename}: {e}')

        self.SFconn.close()