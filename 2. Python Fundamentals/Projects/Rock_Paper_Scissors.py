import random

rock = "rock"
paper = "paper"
scissors = "scissors"

games = int(input(f"How many games do you want to play?: "))

for i in range(games):
    player_move = input("Choose rock, paper or scissors: ")
    if player_move == "rock":
        player_move = rock
    elif player_move == "paper":
        player_move = paper
    elif player_move == "scissors":
        player_move = scissors
    else:
        print("Invalid input. Try again...")
        exit()

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print("You win! Congratulations!")
    elif (player_move == rock and computer_move == paper) or (player_move == paper and computer_move == scissors) or \
            (player_move == scissors and computer_move == rock):
        print("You lose! Try again!")
    else:
        print("Draw! Your move is equal to the computer's. Try again!")