import random
n=random.randint(1,101)
a=-1
guesses=0

while (a!=n):
    guesses+=1

    a=int(input("Guess the number : "))

    if(a>n):
        print("The number is lower")

    elif(a<n):
        print("The number is higher")


print(f"----GAME OVER!!! in {guesses} guesses------")




