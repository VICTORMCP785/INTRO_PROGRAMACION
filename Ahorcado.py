def Ahorcado(x):
    palabra=[]
    intentos=7
    Resolver=[]
    Respuestas=''
    Ruta="C:/Users/vcict/Documents/IDV-Primer-Cuatri/Ahorcado.txt"
    print("hola", x, "tienes 7 intentos para adivinar la palabra\nSuerte! ")
    import random
    with open(Ruta) as f:
        for linea in f:
            palabra.append(linea)
    
    Respuesta = random.choice(palabra)
    
    for letras in Respuesta:
        Resolver.append(letras)
    Resolver.remove("\n")
    #print(Resolver) pd. Si quitan el "#" y estas letras se vera la respuesta.
    
    while intentos > 0:
        Fallo=0
        
        for caracteres in Resolver:
            if caracteres in Respuestas:
                print(caracteres,end="")
            else:
                print("_",end="")
                Fallo=Fallo+1
        
        if Fallo==0 :
            print("\nganaste")
            break
        
        Letra_Usuario=input("\nIntroduce una letra en MAYUSCULA: ")
        Respuestas+=Letra_Usuario
        
        if Letra_Usuario not in Resolver:
            intentos=intentos-1
            print("te quedan:",intentos,"intentos")
    print("PERDISTE la respuesta era --->",Respuesta)
Ahorcado(input("Introduce tu nombre: "))