import py42.sdk
import py42.services
import csv
import os
import typer
from datetime import datetime

app = typer.Typer()

host = os.environ.get('CP_HOST', '')
username = os.environ.get('CP_USER', '')
password = os.environ.get('CP_PASSWD', '')
report_date = datetime.now().strftime('%Y-%m-%d')


@app.command()
def get_full_disk_access(
    host:str = host,
    username:str = username,
    password:str = password,
    report_name: str = f"crashplan-fda-{report_date}.csv",
    ):
    """Generate a CSV Report of Devices in All Orgs where full disk access is false"""

    sdk = py42.sdk.from_local_account(host, username, password)
    response = sdk.orgs.get_all(active=True)

    report = []

    for page in response:
        for org in page['orgs']:
            org_id = org['orgId']
            statuses = sdk.orgs.get_agent_full_disk_access_states(org_id).data # change to `devices.get_all` for other things

            # Logic below would need to change based on the request
            for status in statuses:

                if isinstance(status, dict):
                    guid = status['deviceGuid']

                    if status['value'] == "false": # condition to show only false entries
                        device_name = sdk.devices.get_by_guid(guid)['name']
                        report.append({
                            'org_name': org['orgName'],
                            'org_id': org_id,
                            'guid': guid,
                            'name': device_name,
                            'status': 'FULL DISK ACCESS DISABLED',
                            })

        with open(report_name, 'w') as csvfile:
            fieldnames = ['org_name', 'org_id', 'name', 'guid', 'status']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in report:
                writer.writerow(row)


if __name__ == "__main__":
    app()
