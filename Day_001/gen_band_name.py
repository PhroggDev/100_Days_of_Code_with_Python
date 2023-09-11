print("""
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    Welcome to Band Name the generator
    You will prompted for two strings
    Please only use letters [A-Z] or [a-z]
    or numbers [0-9]
    If any input is over 12 characters long you will be prompted
    for a new value
    =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
    """)


# def gen_name(): ## Proper python workflow we would more likely to code a
# series of functions to be called by a main() function
# This exercise just calls for simple inputs and outputs with no validation of
# inputs

first_word = input("Please enter the name of the city or town you were born in: ")
second_word = input("Please enter the name you called your first pet: ")
print("Your home-town band might be named")
print(first_word, second_word)
