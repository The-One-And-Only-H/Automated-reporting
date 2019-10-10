import pymysql
import os
import sys
import time
import re
from slack import WebClient

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
        db='tpa_2020_production') 

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

    rec = curs.fetchone()

    msg = "\n".join(f'{d[0]}: {v}' for (d, v) in zip(curs.description, rec))

    try:
      slack_token = os.environ['TPA_SLACK_TOKEN']
    except KeyError:
      print("Please specify the TPA_SLACK_TOKEN env var", file=sys.stderr)
      sys.exit(1)

    slack_client = WebClient(slack_token)

    slack_client.chat_postMessage(channel="tpa-2020", text="Nominations:\n" + msg)

    curs.execute("""SELECT country, COUNT(*) AS nominations FROM nominations GROUP BY country ORDER BY COUNT(*) DESC""")

    rec = curs.fetchall()

    msg2 = "\n".join('%s: %s' % (country or "Undefined", num) for country, num in rec)

    slack_client.chat_postMessage(channel="tpa-2020", text="Countries:\n" + msg2)

if __name__ == '__main__':
    main()

