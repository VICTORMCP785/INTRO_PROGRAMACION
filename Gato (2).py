import random
#inputs equivocados
#explota al acabar
#isnumeric
def Gato():
	Y=int(input("introduzca el numero de jugadores (maximo 2) si quieres salir coloca 0: "))

	while Y > 2:
		print("Numero No Valido Chaval")
		Y=int(input("introdusca el numero de jugadores (maximo 2) si quieres salir coloca 0: "))
	if Y == 1:
		Solo()
	if Y == 2:
		PVP()
	if Y == 0:
		Exit()
	
def Solo():
	print("Un jugador")        
	NombreJ1=input("introduce tu nombre Jugador 1: ")
	archivo=("C:/Users/Lab 4 Alumno 5/Desktop/Gato/Archivo_Examen_Parcial_2.txt") 
	Lista=[]
	movimientos=1
	Tablero=[0,1,2,3,4,5,6,7,8]

	print (Tablero [0], "|" , Tablero [1], "|" , Tablero [2])
	print ("----------")       
	print (Tablero [3], "|" , Tablero [4], "|" , Tablero [5])
	print ("----------")  
	print (Tablero [6], "|" , Tablero [7], "|" , Tablero [8])

	with open(archivo) as Victoria:
		for Num in Victoria:
			Num=int(Num)
			Lista.append(Num)

	while movimientos <= 9:   
		print("Tu Turno", NombreJ1)
		J1=int(input("coloque el numero de casilla donde quiere colocar: "))
		while J1 not in Tablero:
			print("Ese Numero Ya Fue Usado o No Es Valido")
			J1=int(input("coloque el numero de casilla donde quiere colocar: "))
		if J1 in Tablero:
			Tablero.pop(J1)
			Tablero.insert(J1,"X")
			movimientos=movimientos+1

		print (Tablero [0], "|" , Tablero [1], "|" , Tablero [2])
		print ("----------")       
		print (Tablero [3], "|" , Tablero [4], "|" , Tablero [5])
		print ("----------")  
		print (Tablero [6], "|" , Tablero [7], "|" , Tablero [8])

		if Tablero[0] == "X" and Tablero[3] == "X" and Tablero[6]=="X" or Tablero[1] == "X" and Tablero[4] =="X" and Tablero[7]=="X" or Tablero[2] == "X" and Tablero[5] == "X" and Tablero[8]=="X":
			print("El Ganador es",NombreJ1)
			
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				Solo()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
			if Tablero[0] == "X" and Tablero[1] == "X" and Tablero[2] == "X" or Tablero[3] == "X" and Tablero[4] == "X" and Tablero[5]=="X" or Tablero[6] == "X" and Tablero[7] == "X" and Tablero[8]=="X":
				print("El Ganador es",NombreJ1)
				Lista[0]=Lista[0]+1
				print(NombreJ1,"lleva",Lista[0],"Victorias")
				archivo=open(archivo,"w")
				archivo.write(str(Lista[0]))
				archivo.write("\n")
				archivo.write(str(Lista[1]))
				archivo.write("\n")
				archivo.write(str(Lista[2]))
				archivo.write("\n")
				archivo.write(str(Lista[3]))
				archivo.close()

			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				Solo()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return

			if  Tablero[0] == "X" and Tablero[4] == "X" and Tablero[8]=="X" or Tablero[2] == "X" and Tablero[4] == "X" and Tablero[6] == "X":
				print("El Ganador es",NombreJ1)
				Lista[0]=Lista[0]+1
				print(NombreJ1,"lleva",Lista[0],"Victorias")
				archivo=open(archivo,"w")
				archivo.write(str(Lista[0]))
				archivo.write("\n")
				archivo.write(str(Lista[1]))
				archivo.write("\n")
				archivo.write(str(Lista[2]))
				archivo.write("\n")
				archivo.write(str(Lista[3]))
				archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				Solo()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
			if movimientos>8:
				print("EMPATE")
				Lista[3]=Lista[3]+1
				print("Total de Empates",Lista[3])
				archivo=open(archivo,"w")
				archivo.write(str(Lista[0]))
				archivo.write("\n")
				archivo.write(str(Lista[1]))
				archivo.write("\n")
				archivo.write(str(Lista[2]))
				archivo.write("\n")
				archivo.write(str(Lista[3]))
				archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				Solo()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return

		print("Turno de la Computadora")
		PC = random.randint(0,8)
		while PC not in Tablero:
			PC = random.randint(0,8)
		print("La computadora eligio: ",PC)
		if PC in Tablero:
			Tablero.pop(PC)
			Tablero.insert(PC,"O")
			movimientos=movimientos+1

		print (Tablero [0], "|" , Tablero [1], "|" , Tablero [2])
		print ("----------")       
		print (Tablero [3], "|" , Tablero [4], "|" , Tablero [5])
		print ("----------")  
		print (Tablero [6], "|" , Tablero [7], "|" , Tablero [8])

		if Tablero[0] == "O" and Tablero[3] == "O" and Tablero[6]=="O" or Tablero[1] == "O" and Tablero[4] =="O" and Tablero[7]=="O" or Tablero[2] == "O" and Tablero[5] == "O" and Tablero[8]=="O":
			print("El Ganador es PC")
			Lista[2]=Lista[2]+1
			print("la comutadora lleva",Lista[2],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				Solo()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
		if Tablero[0] == "O" and Tablero[1] == "O" and Tablero[2] == "O" or Tablero[3] == "O" and Tablero[4] == "O" and Tablero[5]=="O" or Tablero[6] == "O" and Tablero[7] == "O" and Tablero[8]=="O":
			print("El Ganador es PC")
			Lista[2]=Lista[2]+1
			print("la computadora lleva",Lista[2],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				Solo()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
		if  Tablero[0] == "O" and Tablero[4] == "O" and Tablero[8]=="O" or Tablero[2] == "O" and Tablero[4] =="O" and Tablero[6]=="O":
			print("El Ganador es PC")
			Lista[2]=Lista[2]+1
			print("la computadora lleva",Lista[2],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				Solo()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return

def PVP():
	print("Dos jugadores")
	NombreJ1=input("introduce tu nombre Jugador 1: ")
	NombreJ2=input("Introduce tu nombre Jugador 2: ")
	movimientos=1
	Tablero=[0,1,2,3,4,5,6,7,8]

	print (Tablero [0], "|" , Tablero [1], "|" , Tablero [2])
	print ("----------")       
	print (Tablero [3], "|" , Tablero [4], "|" , Tablero [5])
	print ("----------")  
	print (Tablero [6], "|" , Tablero [7], "|" , Tablero [8])

	

	while movimientos <= 9:
		print ("tu turno",NombreJ1)
		J1=int(input("coloque el numero de casilla donde quiere colocar: "))
		while J1 not in Tablero:
			print("Ese Numero Ya Fue Usado o No Es Valido")
			J1=int(input("coloque el numero de casilla donde quiere colocar: "))
		if J1 in Tablero:
			Tablero.pop(J1)
			Tablero.insert(J1,"X")
			movimientos=movimientos+1

		print (Tablero [0], "|" , Tablero [1], "|" , Tablero [2])
		print ("----------")       
		print (Tablero [3], "|" , Tablero [4], "|" , Tablero [5])
		print ("----------")  
		print (Tablero [6], "|" , Tablero [7], "|" , Tablero [8])

		if Tablero[0] == "X" and Tablero[3] == "X" and Tablero[6]=="X" or Tablero[1] == "X" and Tablero[4] =="X" and Tablero[7]=="X" or Tablero[2] == "X" and Tablero[5] == "X" and Tablero[8]=="X":
			print("El Ganador es",NombreJ1)
			Lista[0]=Lista[0]+1
			print(NombreJ1,"lleva",Lista[0],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				PVP()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
		if Tablero[0] == "X" and Tablero[1] == "X" and Tablero[2] == "X" or Tablero[3] == "X" and Tablero[4] == "X" and Tablero[5]=="X" or Tablero[6] == "X" and Tablero[7] == "X" and Tablero[8]=="X":
			print("El Ganador es",NombreJ1)
			Lista[0]=Lista[0]+1
			print(NombreJ1,"lleva",Lista[0],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				PVP()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
		if  Tablero[0] == "X" and Tablero[4] == "X" and Tablero[8]=="X" or Tablero[2] == "X" and Tablero[4] =="X" and Tablero[6]=="X":
			print("El Ganador es",NombreJ1)
			Lista[0]=Lista[0]+1
			print(NombreJ1,"lleva",Lista[0],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				PVP()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
		if movimientos>8:
			print("EMPATE")
			Lista[3]=Lista[3]+1
			print("Total de Empates",Lista[3])
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				PVP()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return

		print("tu turno", NombreJ2)
		J2=int(input("coloque el numero de casilla donde quiere colocar: "))
		while J2 not in Tablero:
			print("Ese Numero Ya Fue Usado o No Es Valido")
			J2=int(input("coloque el numero de casilla donde quiere colocar: "))
		if J2 in Tablero:
			Tablero.pop(J2)
			Tablero.insert(J2,"O")
			movimientos=movimientos+1

		print (Tablero [0], "|" , Tablero [1], "|" , Tablero [2])
		print ("----------")       
		print (Tablero [3], "|" , Tablero [4], "|" , Tablero [5])
		print ("----------")  
		print (Tablero [6], "|" , Tablero [7], "|" , Tablero [8])

		if Tablero[0] == "O" and Tablero[3] == "O" and Tablero[6]=="O" or Tablero[1] == "O" and Tablero[4] =="O" and Tablero[7]=="O" or Tablero[2] == "O" and Tablero[5] == "O" and Tablero[8]=="O":
			print("El Ganador es",NombreJ2)
			Lista[1]=Lista[1]+1
			print(NombreJ2,"lleva",Lista[1],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				PVP()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
		if Tablero[0] == "O" and Tablero[1] == "O" and Tablero[2] == "O" or Tablero[3] == "O" and Tablero[4] == "O" and Tablero[5]=="O" or Tablero[6] == "O" and Tablero[7] == "O" and Tablero[8]=="O":
			print("El Ganador es",NombreJ2)
			Lista[1]=Lista[1]+1
			print(NombreJ2,"lleva",Lista[1],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				PVP()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return
		if  Tablero[0] == "O" and Tablero[4] == "O" and Tablero[8]=="O" or Tablero[2] == "O" and Tablero[4] =="O" and Tablero[6]=="O":
			print("El Ganador es",NombreJ2)
			Lista[1]=Lista[1]+1
			print(NombreJ2,"lleva",Lista[1],"Victorias")
			archivo=open(archivo,"w")
			archivo.write(str(Lista[0]))
			archivo.write("\n")
			archivo.write(str(Lista[1]))
			archivo.write("\n")
			archivo.write(str(Lista[2]))
			archivo.write("\n")
			archivo.write(str(Lista[3]))
			archivo.close()
			volver_a_jugar=input("¿Quieres volver a jugar? ")
			if volver_a_jugar == "Si" or volver_a_jugar == "si" or volver_a_jugar =="SI":
				PVP()
			if volver_a_jugar == "No" or volver_a_jugar =="no" or volver_a_jugar =="NO":
				print("Bye Bye")
				return

def Tablerito():
	print (Tablero [0], "|" , Tablero [1], "|" , Tablero [2])
	print ("----------")       
	print (Tablero [3], "|" , Tablero [4], "|" , Tablero [5])
	print ("----------")  
	print (Tablero [6], "|" , Tablero [7], "|" , Tablero [8])

def Exit():
    print("Bye Bye")

def EscrituraP1():
    archivo=("Archivo_Examen_Parcial_2.txt") 
    Lista=[]
    with open(archivo) as Victoria:
        for Num in Victoria:
            Num=int(Num)
            Lista.append(Num)
    Lista[0]=Lista[0]+1
    print(NombreJ1,"lleva",Lista[0],"Victorias")
    archivo=open(archivo,"w")
    archivo.write(str(Lista[0]))
    archivo.write("\n")
    archivo.write(str(Lista[1]))
    archivo.write("\n")
    archivo.write(str(Lista[2]))
    archivo.write("\n")
    archivo.write(str(Lista[3]))
    archivo.close()


Gato() 