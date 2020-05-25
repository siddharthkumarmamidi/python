import sys
def rockpaperscissors():
    user1=input("what's your name")
    user2=input("and your name")
    user1ans=input("%s, do you want to choose rock,paper,scissors?" %user1)
    user2ans=input("%s, do you want to choose rock,paper,scissors?" %user2)
    if user1ans==user2ans:
        return "it's tie"
    elif user1ans=="rock":
        if user2ans=="paper":
            return "user2 won"
        else:
            return "user1 won"
    elif user1ans=="paper":
        if user2ans=="scissors":
            return "user2 won"
        else:
            return "user1 won"
    elif user1ans=="scissors":
        if user2ans=="rock":
            return "user2 won"
        else:
            return "user1 won"
    else:
        print("invalid input, You did,'t choose the option in between rock,paper,scissors")
        sys.exit()
print(rockpaperscissors())
