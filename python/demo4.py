''' Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
them, print out a message of congratulations to the winner, and ask if the players want to start
a new game)
Remember the rules:
 Rock beats scissors
 Scissors beats paper
 Paper beats rock'''

player1 = input("enter the player1 name")
player2 = input("enter the player2 name")
player1_choose = str(input("do you want to choose rock,paper or scissors:"))
player2_choose = str(input("do you want to choose rock,paper or scissors:"))


def compare(p1, p2):
    if p1 == p2:
        return "its a draw"
    elif p1 == 'rock':
        if p2 == 'scissors':
            return "rock wins"
        else:
            return "paper wins"
    elif p1 == 'scissors':
        if p2 == 'paper':
            return "scissors wins"
        else:
            return "rock wins"
    elif p1 == 'paper':
        if p2 == 'rock':
            return "paper wins"
        else:
            return "scissors wins"


print(compare(player1_choose, player2_choose))
