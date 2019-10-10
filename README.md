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
