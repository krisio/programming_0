from random import randint

n = input("How many sides of the dice?")
n = int(n)

dice = randint(1,n)
print("You threw:" +str(dice))
