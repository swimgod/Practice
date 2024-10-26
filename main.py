import argparse
from pathlib import Path, PurePath

from src.tech_interviews.Snowflake import Snowflake


def snowflake_example():
    query_map = {
        'District': './src/tech_interviews/QueryFiles/District',
        'Internal': './src/tech_interviews/QueryFiles/Internal'
    }

    ap = argparse.ArgumentParser()
    ap.add_argument('--filePath', '-f',
                    nargs='*',
                    help='Run all Internal or District query file path(s)')

    args = ap.parse_args(f"--filePath {query_map['District']} {query_map['Internal']}".split())
    reports = Snowflake(args)
    reports.process_files()


if __name__ == "__main__":
    print("hello")