print   """                                                    """
print   """                        Bienvenido a Guess Number"""
print   """           -El juego consiste en adivinar un numero de 1 a 20"""
print   """           -Tiene Cuatro oportunidades para adivinar el numero"""
print   """                                                    """
print   """                                                    """
import random 
nuevo = True
while nuevo == True:
	contador = 1 
	turno = 4
	nuevoJuego = " "
	generado = random.randrange(1,21)
	while contador <= 4:   
		print "\nGenerated:" + str(generado)
		ingresado = raw_input("Numero de 1 a 20\n")
		try:
			ingresado = int(ingresado)
			print "\nGenerado:" + str(generado)
			print "Numero:" + str(ingresado)
			if ingresado > generado:
				contador += 1
				turno -= 1
				print "El numero ingresado es MAYOR al numero generado"
				print "Faltan " + str(turno) + " intentos"
				if turno == 0:
					print "GAME OVER"
					nuevo2 = True
					while nuevo2 == True:
						nuevoJuego = raw_input("Desea jugar de nuevo y/n\n")
						minu = nuevoJuego.lower()
						if minu == "y":
							nuevo = True
							nuevo2 = False
						elif minu == "n": 
							nuevo2 = False
							nuevo = False
							print "GRACIAS POR JUGAR THE GUESS NUMBER"
						else: 
							nuevo2 = True
			elif ingresado < generado:
				contador += 1
				turno -= 1 
				print "El numero ingresado es MENOR al numero generado "
				print "Faltan " + str(turno) + " intentos"
				if turno ==0:
					print "GAME OVER"
					nuevo2 = True
					while nuevo2 == True:
						nuevoJuego = raw_input("Desea jugar de nuevo y/n\n")
						minu = nuevoJuego.lower()
						if minu == "y":
							nuevo = True
							nuevo2 = False
						elif minu == "n": 
							nuevo2 = False
							nuevo = False
							print "GRACIAS POR JUGAR THE GUESS NUMBER"
						else: 
							nuevo2 = True				
			else:
				print "YOU WIN"
				nuevo = False
				nuevo2 = True
				while nuevo2 == True:
					nuevoJuego = raw_input("Desea jugar de nuevo y/n\n")
					minu = nuevoJuego.lower()
					if minu == "y":
						nuevo = True
						nuevo2 = False
					elif minu == "n": 
						nuevo2 = False
						nuevo = False
						print "GRACIAS POR JUGAR THE GUESS NUMBER"
					else: 
							nuevo2 = True
				break
		except:
			print "Lo siento no es un numero, intente de nuevo! Numeros de 1 a 20"	



			

					
			



