import random
choice_taken= ["rock", "paper", "scissor"]
# your name
playerchoice=input("your name")
# no. of rounds
n=int(input("No of rounds you want to play"))
#game playing loop
while True:
    print("THE GAME BEGINS")
    playerscore = 0
    computerscore = 0
    for i in range (1,n+1):
        print("The round", i, "begins")
        print("choose")
        print("1.rock","2.paper","3.scissor")
        player_choice = int(input("playerchoice in integer choice:"))
        if player_choice == 1:
            print("rock")
            player_choice = "rock"
        elif player_choice == 2:
            print("paper")
            player_choice = "paper"
        elif player_choice == 3:
            print("scissor")
            player_choice = "scissor"
        else:
            print("none of the choice chosen")
            break
#computer random choice
        computer_choice = random.choice(choice_taken)
        print("computer taken :", computer_choice)
#tie condition
        if player_choice == computer_choice:
            print("its a tie", "both go home and do practice")
#winning condition
        elif (player_choice == "paper" and computer_choice == "rock" ) or (player_choice == "rock" and computer_choice == "scissor" ) or (player_choice == "scissor" and computer_choice == "paper" ):
            print(playerchoice,"won the round")
            playerscore = playerscore + 1
        else:
            print("computer won the round")
            computerscore = computerscore + 1
    if playerscore > computerscore:
        print(playerchoice, "won the game", "playerscore" ,playerscore  , "computerscore", computerscore )
    elif computerscore > playerscore:
        print("computer won the whole game", "playerscore",playerscore, "computerscore", computerscore)
#restarting or ending the game
    player = input("want to play again for the revenge?")
    if player == "yes":
        continue
    else:
        print("THE GAME ENDS HERE")
        break
