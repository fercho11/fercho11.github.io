#Script que juega Piedra, Papel o Tijera con el usuario
import random 

#Leer eleccion del Usuario
user = input("Elige: Piedra, Papel o Tijera \n ")

#Generar eleccion de la Maquina
aleatorio = random.randint (1, 3)
if aleatorio == 1:
    machine = "piedra"
elif aleatorio == 2:
    machine = 'papel'
else:
    machine = 'tijera'

#Comparar para determinar quien gana

print (f"EL usuario eligio {user} y la maquina eligio {machine}")

if user == 'piedra' and machine =='papel':
    print ("Gana la Maquina")
elif user == 'papel' and machine == 'papel':
    print ("Empate")
elif user == 'tijera' and machine == 'papel':
    print ("Gana el Usuario")

elif user == 'piedra' and machine == 'tijera':
    print ("Gana el Usuario")
elif user =='papel' and machine == 'tijera':
    print ("Gana la Maquina")
elif user == 'tijera' and machine == 'tijera':
    print("Empate")

elif user == 'piedra' and machine == 'piedra':
    print ("Empate")
elif user =='papel' and machine == 'piedra':
    print ("Gana el Usuario")
elif user == 'tijera' and machine == 'piedra':
    print("Gana la Maquina")
else:
    print('Escribe bien tu eleccion')
