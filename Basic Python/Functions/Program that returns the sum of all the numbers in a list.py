def sum_all_numbers_from_a_list(the_list): 
	total_sum = 0
	for index in range(len(the_list)):
		total_sum += the_list[index] 
	return total_sum


numbers = [4, 6, 2, 29]
result = sum_all_numbers_from_a_list(numbers)
print(result)