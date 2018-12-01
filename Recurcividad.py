def Recurcividad(Num1,Num2,Repetición):
    if Num1==Multi:
        print(Num1)
    elif Num1!=Num1*Num2:
        Num1=Num1+Repetición
        Recurcividad(Num1,Num2,Repetición)
Num1=int(input("Num1 "))
Num2=int(input("Num2 "))
Repetición=Num1
Multi=Num1*Num2
Recurcividad(Num1,Num2,Repetición)