list_a = ["first_name", "last_name", "role"]
list_b = ["Thomas", "Perez", "Software Engineer"]
developer = {}

for i in range(len(list_a)):          
    developer[list_a[i]] = list_b[i]            
print(developer)