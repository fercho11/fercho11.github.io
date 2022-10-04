def suma (num1, num2):
    return num1 + num2

def resta (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

def return_values ():
    num1 = v1
    num2 = v2
    return_values v1, v2

if __name__ == 'main':
    message = f"Calculadora:\n Elige una opcion\n 1 - suma\n 2 - resta\n 3 - multiplicacion\n 4 - Divicionn\n 5 - Salir\n"
    while True:
        opcion = int (input (message))
        #comparar cada de las opciones y llamar a la funcion que corresponda
        if = opcion == 1:
            #Pedir valores al usuario
            resultado_suma = suma (v1, v2)
            print ("EL resultado de la suma es", resultado_suma)
        elif opcion == 2:
            #Pedir valores al usuario
            resultado_resta = resta (v1, v2)
            print ("EL resultado de la resta es", resultado_resta)
        if = opcion == 3:
            #Pedir valores al usuario
            resultado_multi = multiply (v1, v2)
            print ("EL resultado de la multiplicacion es", resultado_multi)
        if = opcion == 4:
            #Pedir valores al usuario
            resultado_div = divide (v1, v2)
            print ("EL resultado de la div es", resultado_div)
        elif opcion == 5:
            print ("Bye!")
            break

        else:
            print ("Opcion incorrecta")