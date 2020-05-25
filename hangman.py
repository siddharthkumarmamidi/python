import turtle
turtle.shape("turtle")
turtle1=turtle
turtle2=turtle
#turtle=None
host=input("hey host, what's your name")
player=input("hey player, what's your name")
secretword=input("%s,choose the secretword" %host)
print("hey player, the length of the secretword is %s" %len(secretword))
guesses=0
a=[0]*len(secretword)
for i in range(len(secretword)):
    a[i]="_"
turtle1.forward(100)
turtle1.backward(50)
turtle1.left(90)
turtle1.forward(150)
turtle1.left(90)
turtle1.forward(70)
turtle1.left(90)
turtle1.forward(20)
turtle1.penup()
wrong_guess=0
while guesses<len(secretword):
    guesses+=1
    guess=input("hey player guess the character now")
    if guess in secretword:
        for i in range(len(secretword)):
            if guess==secretword[i]:
                #print("hurray, right guess")
                if a[i].isalpha():
                    pass
                else:
                    a[i]=guess
                    used=print(' '.join(a))
    else:
        wrong_guess+=1
        print("sorry wrong guess")
        if wrong_guess==1:
            turtle1.forward(20)
            turtle1.pendown()
            turtle1.left(90)
            turtle1.circle(10)
            turtle1.hideturtle()
        elif wrong_guess==2:
            turtle1.right(90)
            turtle1.forward(45)
            turtle1.backward(30)
            turtle1.right(45)
            turtle1.forward(30)
            turtle1.hideturtle()
        elif wrong_guess==3:
            turtle1.backward(30)
            turtle1.left(90)
            turtle1.forward(30)
            turtle1.hideturtle()
        elif wrong_guess==4:
            turtle1.backward(30)
            turtle1.right(45)
            turtle1.forward(50)
            turtle1.right(45)
            turtle1.forward(30)
            turtle1.hideturtle()
        elif wrong_guess==5:
            print('the person gonna hanged completly if u give another wrong guess')
        else:
            turtle1.backward(30)
            turtle1.left(90)
            turtle1.forward(30)
            turtle1.hideturtle()

    if ''.join(a)==secretword:
        print("yaaaaaaay you guessed the right word")
        break
if ''.join(a)!=secretword:
    print("sorry, the person is dead now")
    turtle1.clear()
    del turtle1
    turtle2.penup()
    turtle2.setpos(0,0)
    turtle2.pendown()#turtle2.left(90+45)
    #turtle2.pendown()
    turtle2.forward(100)
    turtle2.backward(50)
    turtle2.left(90)
    turtle2.forward(150)
    turtle2.left(90)
    turtle2.forward(70)
    turtle2.left(90)
    turtle2.forward(20)
    turtle2.penup()
    turtle2.forward(20)
    turtle2.pendown()
    turtle2.left(90)
    turtle2.circle(10)
    turtle2.right(90)
    turtle2.forward(45)
    turtle2.backward(30)
    turtle2.right(45)
    turtle2.forward(30)
    turtle2.backward(30)
    turtle2.left(90)
    turtle2.forward(30)
    turtle2.backward(30)
    turtle2.right(45)
    turtle2.forward(50)
    turtle2.right(45)
    turtle2.forward(30)
    turtle2.backward(30)
    turtle2.left(90)
    turtle2.forward(30)
    turtle2.hideturtle()
