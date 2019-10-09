import pymysql
import os
import sys
import csv

def main():
    try:
      password = os.environ['TPA_DB_PASSWORD']
    except KeyError:
      print("Please specify the TPA_DB_PASSWORD env var", file=sys.stderr)
      sys.exit(1)
    
    connection = pymysql.connect(host='5.57.62.164',
        user='tpaDBAdmin',
        password=password,
        charset='utf8mb4',
        db='tpa_2020_staging')

    curs = connection.cursor()

    curs.execute("""SELECT
        A AS 'Role Model',
        B AS 'Rising Technologist',
        C AS 'Business Leader',
        D AS 'Employer Award',
        E AS 'Technology Innovator',
        F AS 'Technology Playmaker of the Year 2020',
        G AS 'Social Impact Award',
        H AS 'Champion of Change',
        I AS 'Academic Achievement',
        J AS 'Entrepreneur Award'
    FROM       (SELECT COUNT(*) AS A FROM `nominations` WHERE `categoryNames` LIKE '%Role Model%') a
    CROSS JOIN (SELECT COUNT(*) AS B FROM `nominations` WHERE `categoryNames` LIKE '%Rising Technologist%') b
    CROSS JOIN (SELECT COUNT(*) AS C FROM `nominations` WHERE `categoryNames` LIKE '%Business Leader%') c
    CROSS JOIN (SELECT COUNT(*) AS D FROM `nominations` WHERE `categoryNames` LIKE '%Employer Award%') d
    CROSS JOIN (SELECT COUNT(*) AS E FROM `nominations` WHERE `categoryNames` LIKE '%Technology Innovator%') e
    CROSS JOIN (SELECT COUNT(*) AS F FROM `nominations` WHERE `categoryNames` LIKE '%Technology Playmaker of the Year 2020%') f
    CROSS JOIN (SELECT COUNT(*) AS G FROM `nominations` WHERE `categoryNames` LIKE '%Social Impact Award%') g
    CROSS JOIN (SELECT COUNT(*) AS H FROM `nominations` WHERE `categoryNames` LIKE '%Champion of Change%') h
    CROSS JOIN (SELECT COUNT(*) AS I FROM `nominations` WHERE `categoryNames` LIKE '%Academic Achievement%') i
    CROSS JOIN (SELECT COUNT(*) AS J FROM `nominations` WHERE `categoryNames` LIKE '%Entrepreneur Award%') j""")

    w = csv.writer(sys.stdout)

    w.writerow(f[0] for f in curs.description)

    for row in curs.fetchall():
        w.writerow(row)

    curs.execute("""SELECT country, COUNT(*) AS nominations FROM nominations GROUP BY country ORDER BY COUNT(*) DESC""")

    w.writerow(f[0] for f in curs.description)

    for row in curs.fetchall():
        w.writerow(row)

if __name__ == '__main__':
    main()

