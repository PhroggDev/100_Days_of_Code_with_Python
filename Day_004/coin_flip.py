import random


def welcome():
    print(
        """Welcome to coin flipper!\n"""
    )


def coin_toss():
    face_val = random.randint(0, 1)
    if face_val == 0:
        return "Heads"
    else:
        return "Tails"


if __name__ == "__main__":
    welcome()
    print("Tossing coin...")
    print(f"You see {coin_toss()} come up!!!")
