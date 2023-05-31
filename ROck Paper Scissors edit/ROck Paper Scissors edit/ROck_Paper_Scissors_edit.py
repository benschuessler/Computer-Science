# Author: Ben Schuessler
# Description: Rock Paper Scissors able to declare winner
# Date submitted: 3/28
# Bugs: Messed up if, elif, else at first
# Challenges: Tell winner, User error
# Sources: W3Schools



import random #makes computer chose a choice randomly
choices = ["rock", "paper","scissors"] #list of choices that user can choose from
scoreplayer = 0
scorecomputer = 0

while True:
    bot_choice = random.choice(choices) #computer chooses randomly from choises (rock,paper, and scissors)
    user_choice = input("Enter stop to end. Rock, paper, scissors, shoot!") #user chooses one choice out of rock paper and scissors
    user_choice = user_choice.lower() #lower() means that capital letters can be used in answer

    if user_choice == ("stop"): #if the user types in stop the code will stop
        break
    
    if user_choice not in choices:
        print("invalid try again")

    else:
        print("Computer chose: " + bot_choice + " You chose: " + user_choice) #sets computer to print the randomly made choice

        if user_choice == bot_choice:
            print("tie")
    
        if user_choice == "rock": #if the user types in rock
            if bot_choice == "scissors": #the bot randomly selects scissors
                print("you win") #print you win because bot chose scissors vs paper making user win
                scoreplayer += 1
            elif bot_choice == "paper": #the bot randomly selects paper
                print("you lose") #print you lose because the bot won by selecting paper
                scorecomputer +=1
        if user_choice == "scissors": #user types in scissors
            if bot_choice == "paper": #the bot randomly selects paper
                print("you win") #pring you win because user selected scissors which beats paper
                scoreplayer += 1
            elif bot_choice == "rock": #bot chooses rock
                 print("you lose") #print you lose because user selected scissors which loses to rock
                 scorecomputer +=1
        
        elif user_choice == "paper": #user types in paper
            if bot_choice == "rock": #bot randomly selects rock
                print("you win") #print you win because user selected paper which beats rock
                scoreplayer += 1
            elif bot_choice == "scissors": #bot randomly selects scissors
                print("you lose") #print you lose because user selected paper which loses to scissors
                scorecomputer +=1
  
        print("player score is:", scoreplayer)
        print("computer score is:", scorecomputer)




