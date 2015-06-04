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
again = True #Creating boolean variable(again) in true
while again == True: #Start the while loop in True, Start all program
	count = 1 #Start counter in (1)
	turn = 4 #The countdown begins in (4)
	newGame = " " #Creating variable(newGame) as string
	generated = random.randrange(1,21) #Creating a random number from 1 to 20
	while count <= 4: #Starts the while loop and runs while(count) is less than five   
		print "\nYou have " + str(turn) + " attempt(s)" #Print the message as many as attemps have
		joined = raw_input("Enter a number from 1 to 20\n") #The player enter the number
		time.sleep(0.5) #The program stops for 0.5 seconds
		try: #Use the function TRY
			joined = int(joined) #Compare if the number is interger
			if joined > generated: #Compare if the number joined is high number generated
				count += 1 #Adds 1 to variable(count)
				turn -= 1 #Rest 1 to variable(turn)
				print "You guessed to HIHG, please try again\n" #Print the message, number high
				time.sleep(0.5) #The program stops 1.5 seconds
				if turn == 0: #Compare if furn is equal to (0)
					print "GAME OVER" #Print Game Over part high
					reagain = True #Create the boolean variable(regain) in true
					while reagain == True: #Starts the while loop and runs while(regain) is True
						newGame = raw_input("Want to play again? y/n\n") #Question to play agian?  
						minuscule = newGame.lower() #The variable(minuscule) lowercase the newGame
						if minuscule == "y": #Comparate if minuscule is same that "y"
							again = True #The variable(again) is True and the while loop(again) follow
							reagain = False #The variable(regain) is False and the while loop(regain) not follow
							os.system("clear") #The function os(clear) cleaning the terminal
							print   """                                                    """ #Game instructions
							print   """                      Welcome to Guess Number""" #Game instructions
							print   """                     *************************""" #Game instructions
							print   """           -The game is to guess the number from 1 to 20""" #Game instructions
							print   """           -You have four chances to guess the number""" #Game instructions
							print   """                                                    """ #Game instructions
						elif minuscule == "n": #Part elif the if comparate minuscule is same "y" question the variable(minuscule) is "n" 
							reagain = False #The while loop(regain) stop
							again = False #The while loop(again) stop
							print "\nThanks for playing GUESS NUMBER!\n" #Print message thanks for playing
						else: #The else of the if variable(minuscule) is same "y"
							reagain = True #The while loop(regain) follow
			elif joined < generated: #Comparate if generated is high joined
				count += 1 #Adds 1 to variable(count)
				turn -= 1 #Rest 1 to variable(turn)
				print "you guessed to LOW, please try again\n" #Print message guess less
				time.sleep(0.5) #The program stops for 0.5 seconds
				if turn == 0: #Compare if furn is equal to (0)
					print "GAME OVER" #Print Game Over part less
					reagain = True #Create the boolean variable(regain) in true
					while reagain == True: #Starts the while loop and runs while(regain) is True
						newGame = raw_input("Want to play again? y/n\n") #Enter question to play agian
						minuscule = newGame.lower() #Varialbe(minuscule) of newGame lowercase
						if minuscule == "y": #Comparate if minuscule is same "y"
							again = True #While loop(again) follow
							reagain = False #While loop(regain) stop
							os.system("clear") #The function os(clear) cleaning the terminal
							print   """                                                    """ #Game instructions
							print   """                      Welcome to Guess Number""" #Game instructions
							print   """                     *************************""" #Game instructions
							print   """           -The game is to guess the number from 1 to 20""" #Game instructions
							print   """           -You have four chances to guess the number""" #Game instructions
							print   """                                                    """ #Game instructions
						elif minuscule == "n": #The part elif, comparate the variable(minuscule) is same "n"
							reagain = False #The while loop(regaom) stop
							again = False #The while loop(again) stop
							print "\nThanks for playing GUESS NUMBER!\n" #Print message thanks for playing
						else: #The part else, if diferent "y" or "n" 
							reagain = True #The while loop(regain) follow				
			else: #The part else of the if variable(generated) and variable(joined) are same
				print "YOU WIN" #Pring you win
				again = False #The while loop(again) follow
				reagain = True #The while loop(regain) stop
				while reagain == True: #Comparate while loop(regain) while is true follow
					newGame = raw_input("Want to play again? y/n\n") #Question to play again?
					minuscule = newGame.lower() #Varialbe(minuscule) of newGame lowercase
					if minuscule == "y": #Comparate variable(minuscule) is same "y"
						again = True #The while loop(again) follow
						reagain = False # The while loop(regain) stop
						os.system("clear") #The function os(clear) cleaning the terminal
						print   """                                                    """ #Game instructions
						print   """                      Welcome to Guess Number""" #Game instructions
						print   """                     *************************""" #Game instructions
						print   """           -The game is to guess the number from 1 to 20""" #Game instructions
						print   """           -You have8 four chances to guess the number""" #Game instructions
						print   """                                                    """ #Game instructions
					elif minuscule == "n": #Comparate minuscule is same "n"
						reagain = False #The while loop(regain) stop
						again = False #The while loop(again) stop
						print "\nThanks for playing GUESS NUMBER!\n" #Print thanks for playing
					else: #This is else of the if minuscule same "y"
							reagain = True #The variable(regain) is true for while loop(regain) follow
				break #Break the while loop(again)			
		except: #This is except of the try
			print "Only numbers please, Try again!"	#Print the message for only numbers



			

					
			



