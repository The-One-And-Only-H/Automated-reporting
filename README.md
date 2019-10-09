The first time you check out the code:

- Create a virtualenv with `virtualenv -p python3 env`
- Install the dependencies using `env/bin/pip install -r requirements.txt`

After which:

- Work in the virtualenv with `source env/bin/activate`
- Export an environment variable with the confidential password: `export TPA_DB_PASSWORD=password`
- Run the script with `python tpa_report.py`
