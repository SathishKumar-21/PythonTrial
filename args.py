def sum_numbers(*n: float) -> float:
    """
    This function returns the sum of integer literals
    :param n: The numbers to get add up
    :return: sum of all value
    """
    return sum(n)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
