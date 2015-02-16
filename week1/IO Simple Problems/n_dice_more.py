from random import randint

n = input("Sides of the dice?")
n = int(n)

dice1 = randint(1,n)
print("First roll:")
print(dice1)
dice2 = randint(1,n)
print("Second roll:")
print(dice2)
dice3 = randint(1,n)
print("Third roll:")
print(dice3)

print("The total sum:")
print(dice1+dice2+dice3)
