
#Creator: Ben Schuessler
#Date 2/27/23
#Description: This code gives responses to questions like an 8 ball
#Sources: Ms Marciano helped me
#Bugs: I set my variables to letters which was confusing and "stop" didn't work at first

import random

responses = ["No", "Yes", "Maybe", "Not Sure as of Now"] # responses after question is random everytime

while True: # creates loop
    question = input("question?") #whatever is typed in is set equal to the variable "question"
    if (question == "stop"): #if type stop code will stop
        break # ending while true loop
    print(random.choice(responses)) #give random response, either ("no", "yes", "maybe", or "not sure as of now"?


