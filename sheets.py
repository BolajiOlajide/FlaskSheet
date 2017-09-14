from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import dotenv

dotenv.load()

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'FLASK SHEET'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_dir = os.path.join('.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def read(credentials):
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = dotenv.get('SHEET_ID')
    rangeName = 'Class Data!A2:C'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        return []
    else:
        result = []
        for row in values:
            # Print columns A and C, which correspond to indices 0 and 4.
            todos = {}
            todos['name'] = row[0]
            todos['description'] = row[1]
            todos['status'] = row[2]
            result.append(todos)
        return result

def write(credentials, values):
    service = discovery.build('sheets', 'v4', credentials=credentials)

    # The ID of the spreadsheet to update.
    spreadsheet_id = dotenv.get('SHEET_ID')  # TODO: Update placeholder value.

    # The A1 notation of the values to update.
    range_ = 'Class Data!A2:C'  # TODO: Update placeholder value.

    value_range_body = {
        # TODO: Add desired entries to the request body. All existing entries
        # will be replaced.
        'values': values
    }

    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, 
        body=value_range_body, valueInputOption="USER_ENTERED")
    response = request.execute()
