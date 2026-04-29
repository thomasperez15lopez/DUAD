import random
secret_number = random.randint(1, 10)  

number_entered_by_user = int(input("Ingresa un número del 1 al 10: "))

while number_entered_by_user != secret_number:
    if number_entered_by_user < secret_number:
        print("Muy bajo")
    else:
        print("Muy alto")
    number_entered_by_user = int(input("inténtalo nuevamente, Ingresa otro número: "))	
print("¡Felicidades! Adivinaste el número secreto")