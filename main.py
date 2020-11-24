# slot_machine.py
# @author David
# Date 11/16/20
# Purpose: random equality operator, while loop, if statements

import random

bet = int(input("How much do you wanna bet?: "))
balance = 500
balance -= bet

print("You're Balance is Now:" + str(balance))
if balance < 0:
    print("You Dont Have Enough Money")

else:
    confirm = input("Are You Sure? (y/n): ")
if confirm == "y":
    slot_one = random.randint(1, 7)
    slot_two = random.randint(1, 7)
    slot_three = random.randint(1, 7)

# printing
print(str(slot_one) + " " + str(slot_two) + " " + str(slot_three))

# winning
if (slot_one == slot_two and slot_two == slot_three):
    print("Jackpot")
    balance += 10000000
else:
    print("Sorry you lose")

# redo
redo = input("Would You Like To Play Again?: ")

while redo == "y":
    bet = int(input("How much do you wanna bet?: "))
    balance -= bet

    print("You're Balance is Now:" + str(balance))

    if balance < 0:
        print("You Dont Have Enough Money")
        break
    else:
        confirm = input("Are You Sure? (y/n): ")

    if confirm == "y":
        slot_one = random.randint(1, 7)
        slot_two = random.randint(1, 7)
        slot_three = random.randint(1, 7)

        # printing
        print(str(slot_one) + " " + str(slot_two) + " " + str(slot_three))

        # winning
        if (slot_one == slot_two and slot_two == slot_three):
            print("Jackpot")
            balance += 10000000
        else:
            print("Sorry you lose")
