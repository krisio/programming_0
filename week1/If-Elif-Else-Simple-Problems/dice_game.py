from random import randint

n = input("Sides of dice:")
n = int(n)

player1 = input("Player 1 name:")
player2 = input("Player 2 name:")

dice1 = randint(1,n)
print(player1, ' rolls', dice1)
dice2 = randint(1,n)
print(player2 , ' rolls' , dice2)

if dice1>dice2:
    print(player1 + ' wins')
elif dice1<dice2:
    print(player2 + ' wins')
elif dice1 == dice2:
    print("Draw")
