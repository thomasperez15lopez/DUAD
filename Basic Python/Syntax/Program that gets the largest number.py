print("---- simulador para obtener el numero mayor ----")

first_number = input("provide me first number: ")
second_number = input("provide me second number: ")
third_number = input("provide me third number: ")


if first_number >= second_number and first_number >= third_number:
    largest = first_number
elif second_number >= first_number and second_number >= third_number:
    largest = second_number
else:
    largest = third_number
print("The largest number is:", largest)