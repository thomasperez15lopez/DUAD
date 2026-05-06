def sum_2_to_any_number(number):
	print("adding 2 to entered number")
	new_number = number + 2
	print(f"inside function: {new_number}")
	return new_number


number = 5
number = sum_2_to_any_number(number)
print("outside using return:", number)

# accessing a defined variable within a function from the outside
print(new_number)