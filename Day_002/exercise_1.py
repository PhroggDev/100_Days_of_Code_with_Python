"""Prompt for user input Type Check for number only of 2 digits Isolate the digits and sum them"""
while True:
    user_input = input("Please submit a two(2) digit number: ")
    if len(user_input) == 2 and user_input.isnumeric():
        break
    else:
        continue

print(f"{user_input[0]} + {user_input[1]} = {int(user_input[0]) + int(user_input[1])}")
