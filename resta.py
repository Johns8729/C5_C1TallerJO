while: 
    num1 = float(input("ingrese el primer numero:  ")) 
    num2 = float(input("ingrese el segundo numero:  "))
    if num1 < 0 or num2 < 0: 
        print("error")

    else: 
        resultado = num1 - num2 
        print(f"la resta es :{resultado}") 
        break
        
