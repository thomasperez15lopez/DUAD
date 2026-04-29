def multiply_by_2_to_lists(numbers):
    index = 0
    while index < len(numbers):
        numbers[index] *= 2
        index += 1   
    print(numbers)	
    add_2_to_lists(numbers)


def add_2_to_lists(number_1):
    for index, value in enumerate(number_1):
        number_1[index] = value + 2
    print(number_1)


numbers = [2, 3, 4]
multiply_by_2_to_lists(numbers)

print(__file__)
