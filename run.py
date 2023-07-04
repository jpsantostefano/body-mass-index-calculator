import gspread
from google.oauth2.service_account import Credentials
from datetime import date

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("body-mass-index")

list = SHEET.worksheet("data")

option = None
table = []
record = None

print("\nWelcome to the BODY-MASS INDEX program\n")

name = input("What's your name?: ")

print(f"\nHi {name}, select one of the option:\n")

while option != 3:
    print("\n1- Calculate your body mass index")
    print("2- See your history")
    print("3- Exit\n")

    option = input("Select an option: ")
    if option == "1":
        while True:
            try:
                weight = float(input("\nWhat's your weight in kg?: "))
                break
            except ValueError:
                print("\nPlease, insert a right value\n")
        while True:    
            try:
                height = float(input("What's your height in cm?: "))
                break
            except ValueError:
                print("\nPlease, insert a right value\n")
                
        imc = round(weight/((height/100)**2),2)
        if imc < 18.49:
            print(f"\nYour body-mass index is {imc} and you are in the lLOW WEIGHT category\n")
        elif imc >= 18.5 and imc <=24.49:
            print(f"\nYour body-mass index is {imc} and you are in the NORMAL RANGE category\n")
        elif imc >= 25 and imc <= 29.99:
            print(f"\nYour body-mass index is {imc} and you are in the OVERWEIGHT category\n")
        else:
            print(f"\nYour body-mass index is {imc} and you are in the OBESE category\n") 
        print("****BODY-MASS INDEX CLASIFICATION****\n")
        print("Low weight: Less than 18.5")
        print("Normal range: 18.5 to 24.99")
        print("Overweight: 25 to 29.99")
        print("Obese: more than 30\n")

        
        while record != "n" and record !="y":
            record = input("Do you want to add this record? Y/N: ")
            record = record.lower()
            
            if record == "y":
                day = date.today()
                today = day.strftime("%d/%m/%Y")
                table.append(today)
                table.append(imc)
                list.append_row(table)
                table = []
                print("Your body-mass index has been saved on the spreadsheet")
                break
            elif record == "n":
                break
            else:
                print("\nInvalid option. Please write the letter 'Y' to save the record or 'N' to go back to the main menu\n")
            

    elif option == "2":
        data = list.get_all_values()
        data = data[1:]
        print("   DATE           BODY-MASS INDEX")
        for row in data:
            print(row[0],"          ",row[1])
    elif option == "3":
        break    
    else:
        print("\nPlease, insert a valid option\n")


