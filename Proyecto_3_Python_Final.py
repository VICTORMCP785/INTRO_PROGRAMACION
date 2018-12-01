def Menu():
    while True:
        Num=str(input("como quiere ordenar promedio o alfabetico\nSi quiere salir precione 0\n"))
        if Num == "alfabetico" or Num == "Alfabetico" or Num == "ALFABETICO":
            alfabetico()
            break
        if Num == "promedio" or Num == "Promedio" or Num == "PROMEDIO":
            calificacion()
            break
        if Num == "0":
            break
        else:
            print("opcion no valida")
def alfabetico():
    Lectura=[]
    archivo="alumnos.txt"
    Registro=[]

    with open(archivo) as alumnos:
        for linea in alumnos:
            Lectura.append(linea)

    for i in range(len(Lectura)):
        for j in range(i+1, len(Lectura)):
            if Lectura[i] > Lectura[j]:
                Lectura[j], Lectura[i] = Lectura[i], Lectura[j]

    print(Lectura)
    for Personas in Lectura:
        Registro.append(Personas.split())

    Escritura(Registro)

    Volver_Ordenar=str(input("Desea ordenar de otra manera a los alumnos? (Si o cualquier cosa = No)\n"))
    if Volver_Ordenar == "Si" or Volver_Ordenar == "si" or Volver_Ordenar == "SI":
        Menu()
    
def calificacion():
    archivo="alumnos.txt"
    Registro=[]
    Lectura=[]

    #Lectura de archivo
    with open(archivo) as alumnos:
        for linea in alumnos:
            Lectura.append(linea)

    #Separa en listas dentro de una lista el contenido de un videojuego
    Nuevo_alumno=str(input("decea introducir un nuevo alumno? (Si o cualquier cosa = No)\n"))
    if Nuevo_alumno == "Si" or Nuevo_alumno == "si" or Nuevo_alumno == "SI":
        Alumnito=str(input("introdusca el alumno con este formato\nNombre_alumno promedio grupo\n"))
        Lectura.append(Alumnito)
    for personas in Lectura:
        Registro.append(personas.split())
    #Loop de reseteo de numero
    for regreso in Lectura:
        Numero=0

        #Numero de veces para salir del for el cual es el numero de personas - 1
        for loop in range((len(Registro))-1):   
            #agrega a una nueva lista ciertas partes de la lista Registro
            R=Registro[Numero]
            R2=Registro[Numero+1]
            if float(R[1])<float(R2[1]):
                #intercambio de partes para el acomodo de mayor a menor
                temp = Registro[Numero]
                Registro[Numero] = Registro[Numero+1]
                Registro[Numero+1] = temp
            Registro[Numero]
            Numero=Numero+1
    print(Registro)

    Escritura(Registro)

    Volver_Ordenar=str(input("Desea ordenar de otra manera a los alumnos? (Si o cualquier cosa = No)\n"))
    if Volver_Ordenar == "Si" or Volver_Ordenar == "si" or Volver_Ordenar == "SI":
        Menu()

def Escritura(Registro):
    
    archivo="alumnos.txt"

    escritura=open(archivo,"w")
    for N in range ((len(Registro))):
        #sobreescritura del archivo
        Lista=Registro[N]
        escritura.write(str(Lista[0]))    
        escritura.write(str(" "))
        escritura.write(str(Lista[1]))
        escritura.write(str(" "))
        escritura.write(str(Lista[2]))
        escritura.write(str("\n"))
    escritura.close()

    Eleccion=str(input("Quiere ordenarlos en grupos? (Si o cualquier cosa = No)\n"))
    if Eleccion=="SI" or Eleccion=="si" or Eleccion=="Si":
        #escritura en diferentes tipos de archivos
        for R in range((len(Registro))):
            Lista=Registro[R]
            Grupos=open(Lista[2]+".txt","w")
        Grupos.close()
        for R in range((len(Registro))):
            Lista=Registro[R]
            Grupos=open(Lista[2]+".txt","a")
            Grupos.write(str(Lista[0]))    
            Grupos.write(str(" "))
            Grupos.write(str(Lista[1]))
            Grupos.write(str(" "))
            Grupos.write(str(Lista[2]))
            Grupos.write(str("\n"))
        Grupos.close()

Menu()
