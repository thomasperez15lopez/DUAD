my_list = [4, 3, 6, 1, 7]
length = len(my_list)

for index in range(length):
    if index == 0:
        my_list[index], my_list[length - 1] = my_list[length - 1], my_list[index]
print(my_list)