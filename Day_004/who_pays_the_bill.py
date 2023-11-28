import random           # yup, random rules the day
from sys import exit


def welcome():
    """A banner to welcome our user"""
    print("Who will pay the bill today...")


def get_names():
    """Method to accept user input
    Throws exit code if no names are entered"""
    name_list = []
    while True:
        name_input = input("Please enter a name (leave blank to quit adding names): ")
        if len(name_list) == 0 and (name_input == '' or name_input == ' '):
            print("Eh eh, no dine and dash allowed!!")
            exit(1)
        if name_input == '' or name_input == ' ':
            break
        name_list.append(name_input)
    return name_list


def get_name(names):
    """Choose a random name from a list passed in"""
    pay_bill = names[random.randint(0, len(names))]
    return pay_bill


if __name__ == "__main__":
    welcome()
    payer = get_name(get_names())
    print(f"Today {payer} will settle the bill for us all!")
