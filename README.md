# CrashPlan (by Code42) Full Disk Access Report Generator

This python script will generate a csv file of all the devices (by org) that do not have full disk
access turned on.

Tested For: Python 3.10 (But should work for 3.7+)

## Quickstart:

* Clone/Fork
* Create Environment Variables for (CP_HOST, CP_USER, CP_PASSWD)
* install requirements `pip install -r requirements.txt`
* run: `python cpfda.py`
* 🥳


## For Help
This project uses typer, you can view the input parameters with `python cpdfa.py --help`

![Output of `python cpdfa.py --help`](./assets/completion.png)

## Variables you can pass in:

### Authentication Variables:
If you don't want to create environment variables for the host(CP_HOST), username(CP_USERNAME), or
password(CP_PASSWD), you can manually pass them in. 

`python cpdfapy --host https://myhost.crashplan.com --username my_username --password my_password` 

### Report Name
By default the report name is
`crashplan-fda-<year>-<month>-<day>.csv

You can pass in a report name:
`python cpfda.py --report-name my-report-name.csv`
