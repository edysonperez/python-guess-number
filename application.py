import random
import os
import time
os.system("clear")
print   """                                                    """
print   """                      Welcome to Guess Number"""
print   """                     *************************""" 
print   """           -The game is to guess the number from 1 to 20"""
print   """           -You have four chances to guess the number"""
print   """                                                    """
time.sleep(2)
again = True
while again == True:
	count = 1 
	turn = 4
	newGame = " "
	generated = random.randrange(1,21)
	while count <= 4:   
		print "\nYou have " + str(turn) + " attempt(s)"
		joined = raw_input("Enter a number from 1 to 20\n")
		time.sleep(0.5)
		try:
			joined = int(joined)
			if joined > generated:
				count += 1
				turn -= 1
				print "You guessed to HIHG, please try again\n"
				time.sleep(0.5)
				if turn == 0:
					print "GAME OVER"
					reagain = True
					while reagain == True:
						newGame = raw_input("Want to play again? y/n\n")
						minuscule = newGame.lower()
						if minuscule == "y":
							again = True
							reagain = False
							
							os.system("clear")
							print   """                                                    """
							print   """                      Welcome to Guess Number"""
							print   """                     *************************"""
							print   """           -The game is to guess the number from 1 to 20"""
							print   """           -You have four chances to guess the number"""
							print   """                                                    """
						elif minuscule == "n": 
							reagain = False
							again = False
							print "\nThanks for playing GUESS NUMBER!\n"
						else: 
							reagain = True
			elif joined < generated:
				count += 1
				turn -= 1 
				print "you guessed to LOW, please try again\n"
				time.sleep(0.5)
				if turn == 0:
					print "GAME OVER"
					reagain = True
					while reagain == True:
						newGame = raw_input("Want to play again? y/n\n")
						minuscule = newGame.lower()
						if minuscule == "y":
							again = True
							reagain = False
							
							os.system("clear")
							print   """                                                    """
							print   """                      Welcome to Guess Number"""
							print   """                     *************************"""
							print   """           -The game is to guess the number from 1 to 20"""
							print   """           -You have four chances to guess the number"""
							print   """                                                    """
						elif minuscule == "n": 
							reagain = False
							again = False
							print "\nThanks for playing GUESS NUMBER!\n"
						else: 
							reagain = True				
			else:
				print "YOU WIN"
				again = False
				reagain = True
				while reagain == True:
					newGame = raw_input("Want to play again? y/n\n")
					minuscule = newGame.lower()
					if minuscule == "y":
						again = True
						reagain = False
						
						os.system("clear")
						print   """                                                    """
						print   """                      Welcome to Guess Number"""
						print   """                     *************************"""
						print   """           -The game is to guess the number from 1 to 20"""
						print   """           -You have four chances to guess the number"""
						print   """                                                    """
					elif minuscule == "n": 
						reagain = False
						again = False
						print "\nThanks for playing GUESS NUMBER!\n"
					else: 
							reagain = True
				break			
		except:
			print "Try again! Only numbers from 1 to 20"	



			

					
			



