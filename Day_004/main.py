import random
from a_module import PI

random_int = random.randint(1, 10)

print(f"Our first number is a random integer {random_int}")
print("importing a constant for PI from adjacent module...")
print(f"Multiplying the two {PI} * {random_int} is {PI * random_int}")
