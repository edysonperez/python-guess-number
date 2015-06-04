""" Guess a Number"""
import random #Import function RANDOM
import os #Import function OS
import time #Import function TIME
os.system("clear") #Cleaning the terminal
print   """                                                    """ #Game instructions
print   """                      Welcome to Guess Number""" #Game instructions
print   """                     *************************""" #Game instructions
print   """           -The game is to guess the number from 1 to 20""" #Game instructions
print   """           -You have four chances to guess the number""" #Game instructions
print   """                                                    """ #Game instructions
time.sleep(2) #The program stops for 2 seconds
AGAIN = True #Creating boolean variable(AGAIN) in true
while AGAIN == True: #Start the while loop in True, Start all program
    COUNT = 1 #Start COUNTer in (1)
    TURN = 4 #The COUNTdown begins in (4)
    NEWGAME = " " #Creating variable(NEWGAME) as string
    GENERATED = random.randrange(1, 21) #Creating a random number from 1 to 20
    while COUNT <= 4: #Starts the while loop and runs while(COUNT) is less than five
        print "\nYou have " + str(TURN) + " attempt(s)" #Print the message as many as attemps have
        JOINED = raw_input("Enter a number from 1 to 20\n") #The player enter the number
        time.sleep(0.5) #The program stops for 0.5 seconds
        try: #Use the function TRY
            JOINED = int(JOINED) #Compare if the number is interger
            if JOINED > GENERATED: #Compare if the number JOINED is high number GENERATED
                COUNT += 1 #Adds 1 to variable(COUNT)
                TURN -= 1 #Rest 1 to variable(TURN)
                print "You guessed to HIHG, please try AGAIN\n" #Print the message, number high
                time.sleep(0.5) #The program stops 1.5 seconds
                if TURN == 0: #Compare if furn is equal to (0)
                    print "GAME OVER" #Print Game Over part high
                    REAGAIN = True #Create the boolean variable(regain) in true
                    while REAGAIN == True: #Starts the while loop and runs while(regain) is True
                        NEWGAME = raw_input("Want to play AGAIN? y/n\n") #Question to play agian?
                        MINUSCULE = NEWGAME.lower() #The variable(MINUSCULE) lowercase the NEWGAME
                        if MINUSCULE == "y": #Comparate if MINUSCULE is same that "y"
                            AGAIN = True #The variable(AGAIN) is True and the while loop(AGAIN) fol
                            REAGAIN = False #The while loop(regain) not follow
                            os.system("clear") #The function os(clear) cleaning the terminal
                            print   """                                                    """ #Game
                            print   """                      Welcome to Guess Number"""
                            print   """                     *************************"""
                            print   """           -The game is to guess the number from 1 to 20"""
                            print   """           -You have four chances to guess the number"""
                            print   """                                                    """
                        elif MINUSCULE == "n": #Comparate MINUSCULE is same "n"
                            REAGAIN = False #The while loop(regain) stop
                            AGAIN = False #The while loop(AGAIN) stop
                            print "\nThanks for playing GUESS NUMBER!\n" #Print thanks for playing
                        else: #The else of the if variable(MINUSCULE) is same "y"
                            REAGAIN = True #The while loop(regain) follow
            elif JOINED < GENERATED: #Comparate if GENERATED is high JOINED
                COUNT += 1 #Adds 1 to variable(COUNT)
                TURN -= 1 #Rest 1 to variable(TURN)
                print "you guessed to LOW, please try AGAIN\n" #Print message guess less
                time.sleep(0.5) #The program stops for 0.5 seconds
                if TURN == 0: #Compare if furn is equal to (0)
                    print "GAME OVER" #Print Game Over part less
                    REAGAIN = True #Create the boolean variable(regain) in true
                    while REAGAIN == True: #Starts the while loop(reagain)
                        NEWGAME = raw_input("Want to play AGAIN? y/n\n") #Enter play again
                        MINUSCULE = NEWGAME.lower() #Varialbe(MINUSCULE) of NEWGAME lowercase
                        if MINUSCULE == "y": #Comparate if MINUSCULE is same "y"
                            AGAIN = True #While loop(AGAIN) follow
                            REAGAIN = False #While loop(regain) stop
                            os.system("clear") #The function os(clear) cleaning the terminal
                            print   """                                                    """
                            print   """                      Welcome to Guess Number"""
                            print   """                     *************************"""
                            print   """           -The game is to guess the number from 1 to 20"""
                            print   """           -You have four chances to guess the number"""
                            print   """                                                    """
                        elif MINUSCULE == "n": #Comparate the variable(MINUSCULE) is same "n"
                            REAGAIN = False #The while loop(regaom) stop
                            AGAIN = False #The while loop(AGAIN) stop
                            print "\nThanks for playing GUESS NUMBER!\n" #Print thanks for playing
                        else: #The part else, if diferent "y" or "n"
                            REAGAIN = True #The while loop(regain) follow
            else: #The part else of the if variable(GENERATED) and variable(JOINED) are same
                print "YOU WIN" #Pring you win
                AGAIN = False #The while loop(AGAIN) follow
                REAGAIN = True #The while loop(regain) stop
                while REAGAIN == True: #Comparate while loop(regain) while is true follow
                    NEWGAME = raw_input("Want to play AGAIN? y/n\n") #Question to play AGAIN?
                    MINUSCULE = NEWGAME.lower() #Varialbe(MINUSCULE) of NEWGAME lowercase
                    if MINUSCULE == "y": #Comparate variable(MINUSCULE) is same "y"
                        AGAIN = True #The while loop(AGAIN) follow
                        REAGAIN = False # The while loop(regain) stop
                        os.system("clear") #The function os(clear) cleaning the terminal
                        print   """                                                    """
                        print   """                      Welcome to Guess Number"""
                        print   """                     *************************"""
                        print   """           -The game is to guess the number from 1 to 20"""
                        print   """           -You have8 four chances to guess the number"""
                        print   """                                                    """
                    elif MINUSCULE == "n": #Comparate MINUSCULE is same "n"
                        REAGAIN = False #The while loop(regain) stop
                        AGAIN = False #The while loop(AGAIN) stop
                        print "\nThanks for playing GUESS NUMBER!\n" #Print thanks for playing
                    else: #This is else of the if MINUSCULE same "y"
                        REAGAIN = True #The while loop(regain) follow
                break #Break the while loop(AGAIN)
        except ValueError: #This is except of the try
            print "Only numbers please, Try AGAIN!"	#Print the message for only numbers
