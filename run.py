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

def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here:")

        sales_data = data_str.split(",") #The string gets split up into a list
        print(sales_data)
        validate_data(sales_data) #Runs the validate function with the sales data

        if validate_data(sales_data):
            print("Data is valid")
            break
    return sales_data

def validate_data(values):
    """
    Inside the try, convers all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")
        return False
        
    
    return True



data = get_sales_data()