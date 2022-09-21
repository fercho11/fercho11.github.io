#Lee la edad de alguien
age = int (input ("Ingresa tu edad: "))

#Resta 2 a esta edad y se llama last_years
last_years = age - 2

#first_years sera igual a los 2 por 10.5
first_years = 2 * 10.5

#Multiplicar los anos restantes (last_years) por 4
last_years = last_years * 4

#Sumar los first_years con el resultado anterior 
age_dog = last_years + first_years

#Imprimir lo siguiente "Tienes 24 anos que equivalen a 78 anos perrunos"
print (f"Tienes {age} anos que equivalen a {age_dog} anos perrunos")
