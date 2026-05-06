print("---- Clasificador de grupos etarios según tu edad ----")

name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
age = int(input("ingresa el numero de tu edad actual: "))

if age <= 2:
    category = "bebé"
elif age <= 11:
    category = "niño"
elif age <= 12:
    category = "preadolescente"
elif age <= 17:
    category = "adolescente"
elif age <= 35:
    category = "adulto joven"
elif age <= 64:  
    category = "adulto"
elif age >= 65:  
    category = "adulto mayor"	

print(f"{name} {last_name}, basado en tu edad, tu categoria es: {category}")