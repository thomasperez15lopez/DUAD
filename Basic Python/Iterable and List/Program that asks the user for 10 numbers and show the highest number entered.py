print(" --------- Cálculo del número más alto entre 10 valores ingresados --------- ")

list_of_number = []

for index in range(1,11):
	number_enter_by_the_user = int(input(f"Digite el número {index}: "))
	list_of_number.append(number_enter_by_the_user)
print("Los números ingresados fueron:", list_of_number)
mayor = max(list_of_number)
print(f"El número más alto es: {mayor}")