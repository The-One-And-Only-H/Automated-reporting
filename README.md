The first time you check out the code:

- Create a virtualenv with `virtualenv -p python3 env`
- Install the dependencies using `env/bin/pip install -r requirements.txt`

After which:

- Work in the virtualenv with `source env/bin/activate`
- Export an environment variable with the confidential password: `export TPA_DB_PASSWORD=password`
- Export an environment variable with the confidential token: `export TPA_SLACK_TOKEN=slack_token`
- Run the script with `python tpa_report.py`

If you want to schedule running the program regularly then you can use this in your crontab:

- `TPA_DB_PASSWORD=<your pass>`
- `TPA_SLACK_TOKEN=<your token>`
- `0 11 * * thu /path/to/here/env/bin/python /path/to/here/tpa_report.py`

Output example:

Nominations:
Role Model: 22
Rising Technologist: 4
Business Leader: 2
Employer Award: 0
Technology Innovator: 5
Technology Playmaker of the Year 2020: 0
Social Impact Award: 9
Champion of Change: 4
Academic Achievement: 0
Entrepreneur Award: 2

Countries:
India: 12
Netherlands: 4
Ireland: 4
United States: 4
Nigeria: 3
Singapore: 2
Morocco: 2
South Africa: 2
France: 2
Russian Federation: 1
Iran, Islamic Republic Of: 1
Belgium: 1
Norway: 1
Portugal: 1
Australia: 1
Undefined: 1
Cameroon: 1
Canada: 1
United Kingdom: 1
Ethiopia: 1
Mexico: 1
Thailand: 1
