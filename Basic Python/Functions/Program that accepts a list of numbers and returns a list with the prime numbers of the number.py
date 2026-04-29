def is_prime(number):
    if number <= 1:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def get_prime_numbers(numbers_list):
    prime_numbers = []

    for number in numbers_list:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers


# Test with your list
numbers = [1, 4, 6, 7, 13, 9, 67]

result = get_prime_numbers(numbers)
print(result)