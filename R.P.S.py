import random

choices  = ['rock','paper','scissors'] 


player = input('Enter Your Choise: ')


computer = random.choice(choices)

print('player:' ,player)

print('computer:',computer)



if player == computer:
    print("It is a Draw!")


elif computer == "rock":
    if player == "paper":
        print("You Win :)")
    elif player == 'scissors':
        print("You Loss :(")


elif computer == "paper":
    if player == "rock":
        print("You Loss :( ")
    elif player == 'scissors':
        print("You Win :) ")


elif computer == "scissors":
    if player == "rock":
        print("You Win :)")
    elif player == 'paper':
        print("You Loss :(")
