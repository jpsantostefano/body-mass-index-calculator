import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("caloriesCounter")

list = SHEET.worksheet("data")
data = list.get_all_values()

food_list = {}
print("Welcome to the calories and protein counter\n")

name = input("Escribe tu nombre: ")

print(f"\nHi {name}, choose one of the options\n")
print("1- Add new food to the data base")
print("2- Show full list")
print("3- Calculate your body mass index\n")

option = input("Option: ")
if option == "1":
    food = input("Write the name of the food: ")
    calories = int(input("How many calories have you eaten?: "))
    food_list[food] = calories
    print(food_list)
elif option == "2":
    print(data)
elif option == "3":
    weight = int(input("What's your weight in kg?: "))
    height = float(input("What's your height in cm: "))
    imc = round(weight/((height/100)**2),2)
    if imc < 18.49:
        print(f"\nYour body-mass index is {imc} and you are in lLOW WEIGHT category\n")
    elif imc >= 18.5 and imc <=24.49:
        print(f"\nYour body-mass index is {imc} and you are in NORMAL RANGE category\n")
    elif imc >= 25 and imc <= 29.99:
        print(f"\nYour body-mass index is {imc} and you are in OVERWEIGHT category\n")
    else:
        print(f"\nYour body-mass index is {imc} and you are in OBESE category\n") 
    print("****BODY-MASS INDEX CLASIFICATION****\n")
    print("Low weight: Less than 18.5")
    print("Normal range: 18.5 to 24.99")
    print("Overweight: 25 to 29.99")
    print("Obese: more than 30")
else:
    print("Invalid option")


