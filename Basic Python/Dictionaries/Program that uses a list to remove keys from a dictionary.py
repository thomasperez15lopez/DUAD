list_of_keys = [ "access_level", "age" ]
employee = {'name': 'Thomas', 'email': 'Thomas@ecorp.com', 'access_level': 5, 'age': 32}

for index in range(len(list_of_keys)):
	employee.pop(list_of_keys[index], None)
print(employee)