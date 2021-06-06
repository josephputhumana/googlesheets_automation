from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import numpy as np

SERVICE_ACCOUNT_FILE = '/path/to/service.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

#The ID of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = 'sheetID'

#Creating a sheetsapi object
service = build('sheets', 'v4', credentials=creds)

#Data range from which you want to take data/ push data
SAMPLE_RANGE_NAME = 'sheet1!A1'

#Call the Sheets API to get data from sheets
result = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()

#Call the Sheets API to push data into sheets
def Export_Data_To_Sheets():
    URL = r'http://bit.ly/drinksbycountry'
    df = pd.read_csv(URL)
    df.replace(np.nan, '', inplace=True)

    response_date = service.spreadsheets().values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        valueInputOption='RAW',
        range='sheet1!A1',
        body=dict(
            majorDimension='ROWS',
            values=df.T.reset_index().T.values.tolist())
    ).execute()

Export_Data_To_Sheets()