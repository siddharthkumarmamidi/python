import random
answer=random.randint(1,21)
print(answer)
guess=int(input("guess the number between 1 to 20"))
if guess>answer:
    print("your guess is high")
elif guess<answer:
    print("your guess is low")
elif guess==answer:
    print("hurray, your guess is right")
else:
    print("enter the number")
