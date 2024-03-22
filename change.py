def change():
    
    expense = 23.75
    money = 100
    
    c1= (int(money-expense))
    c2= (float(money-expense))
    c3= int((c2-c1)*100)
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(c1)
    print("Centavos: ")
    print(c3)
