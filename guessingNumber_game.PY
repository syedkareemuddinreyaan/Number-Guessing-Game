import random

target = random.randint(1,100)

while True:
    guess = input("enter a choice or quit(Q) : ")
    if(guess == "Q"):
        break
    guess = int(guess)
    if(guess == target):
        print(f"well done youve guessed the correct number {guess} == {target}")
        break
    elif(guess > target):
        print("please select a smaller number")
    elif(guess < target):
        print("please select a graeater number")

print("-------game over--------")  