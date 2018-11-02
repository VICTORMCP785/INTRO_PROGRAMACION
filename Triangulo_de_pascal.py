def pascal(x):
    fila=x
    inicio=1
    valor=0
    triangulo=[1]
    pascal=[]
    print (triangulo)
    while inicio < fila:
        valor=0
        for numeros in triangulo:
            resultado=(valor+numeros)
            pascal.append(resultado)
            valor=numeros
        triangulo.clear()
        pascal.append(1)
        print(pascal)
        for numbers in pascal:
            triangulo.append(numbers)
        pascal.clear()
        inicio=inicio+1
        
        
pascal(int(input("Coloca el limite de lineas en del triangulo: ")))