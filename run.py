# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread #Library for classes and methods
from google.oauth2.service_account import Credentials #Imports credentials class from service_account function, For google sheets to access our creds.json

#What we want to access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
#Our credentials to get access
CREDS = Credentials.from_service_account_file('creds.json')
#Our credentials applied to only what we want access
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
#Telling gspread our credentials and what we want to access
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
#Creating the sheet from our love_sandwiches file on google sheets
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

#sales variable is now the same as the google sheet tab "sales"
sales = SHEET.worksheet('sales')
#Grabs all the values inside the sales tab
data = sales.get_all_values()

print(data)