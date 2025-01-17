/*{
    "district": "district_name",
    "attachData": true,
    "toGDrive": true,
    "toNotify": "email@email.com",
    "rType": "report_type"
}*/
--

SELECT
  U.SCHOOLCDS,
  COUNT(DISTINCT U.UUID) AS "# Of Students That Are CSU Eligible & Have Not Applied"
FROM STU U
JOIN (
  SELECT
    UUID
  FROM COLLEGE_APPLICATIONS
  WHERE APPLICATIONTYPE != 'Cal State Apply'
  AND APPLICATIONSTATUS NOT IN ('Complete', 'In Progress')
) C
ON U.UUID=C.UUID
WHERE U.ELIGIBLE = '1'
AND C.UUID IS NOT NULL
GROUP BY U.SCHOOLCDS