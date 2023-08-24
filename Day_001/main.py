from os import environ


username = environ.get("USER")
print(f"Your username is: {username}")
print(f"There are {len(username)} characters in your username")
