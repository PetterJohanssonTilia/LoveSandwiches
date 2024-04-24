# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread #Library for classes and methods
from google.oauth2.service_account import Credentials #Imports credentials class from service_account function, For google sheets to access our creds.json
from pprint import pprint # example:pprint(data) can be used to easier see the data print in the terminal

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
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers seperated
    by commas, the loop will repeatedly request data, until it is valid.
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
    Inside the try, converts all string values into integers.
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

#def update_sales_worksheet(data):
#    """
#    Update sales worksheet, add new row with the list data provided
#    """
#    print("Updating sales worksheet...\n")
#    sales_worksheet = SHEET.worksheet("sales") #Selects the worksheet
#    sales_worksheet.append_row(data) #Creates a row in the worksheet with the new data
#    print("Sales worksheet updated successfully.\n")

#def update_surplus_worksheet(data):
#    """
#    Update surplus worksheet, add new row with the list data provided
#    """
#    print("Updating surplus worksheet...\n")
#    surplus_worksheet = SHEET.worksheet("surplus") #Selects the worksheet
#    surplus_worksheet.append_row(data) #Creates a row in the worksheet with the new data
#    print("Surplus worksheet updated successfully.\n")

def update_worksheet(data, worksheet):
    """
    Reacieves a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet) #Selects the correct worksheet
    worksheet_to_update.append_row(data) #Creates a row in the worksheet with the new data
    print(f"{worksheet} worksheet updated successfully\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra sandwiches made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values() #stock is the worksheet stock
    stock_row = stock[-1] #Stock_row is now the last row of the stock worksheet
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales #made stock into an integer in this calculation
        surplus_data.append(surplus)
    
    return surplus_data 

def get_last_5_entries_sales():
    """
    Collects collumns of data from sales worksheet, collecting
    the last 5 entires for each sandwich and returns the data
    as a list of lists
    """
    sales = SHEET.worksheet("sales")
    columns = []
    for ind in range(1, 7): 
        column = sales.col_values(ind) # finds the values in a column, go through columns 1-6 in the 'sales' worksheet
        columns.append(column[-5:]) #adds the last 5 value of each column into the columns list, as 5 list containing strings
    return columns


def main():
    """
    Run all program functions
    """
    data = get_sales_data() #data is the users input data
    sales_data = [int(num) for num in data] #sales_data is data but in integers
    update_worksheet(sales_data, "sales") #Updates the worksheet with sales_data
    new_surplus_data = calculate_surplus_data(sales_data) #calculates the surplus by comparing stock vs sales
    update_worksheet(new_surplus_data, "surplus") #Updates the worksheet with sales_data
    



#============== Start ============#
print("Welcome to Love Sandwiches Data Automation")
#main()
sales_columns = get_last_5_entries_sales()