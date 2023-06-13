# def factorial(n: int) -> int:
#     """
#     Return the factorial value of `n`
#     """
#     if n <= 1:
#         return 1
#     result = 2
#     for f in range(3, n + 1):
#         result *= f
#     return result


def factorial(n: int) -> int:
    """
    Return the factorial value of `n`
    """
    if n <= 1:
        return 1
    return n * factorial(n-1)


for i in range(6):
    print(i, factorial(i))
