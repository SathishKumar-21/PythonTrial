from functions import guess_binary

LOW = 1
HIGH = 100

#
# def guess_binary(answer: int, low: int, high: int) -> int:
#     """
#     This function returns the number of guesses of an integer that passes as answer by binary searching method.
#     :param answer: The value needed to find in this guess function
#     :param low: lower limit
#     :param high: higher limit
#     :return: `int` value of guess number made to find the answer in the given limit
#     """
#     guesses = 1
#     while True:
#         guess = low + (high - low) // 2
#         if guess < answer:
#             low = guess + 1
#         elif guess > answer:
#             high = guess - 1
#         elif guess == answer:
#             return guesses
#         guesses += 1
#

max_guesses = 0
correct_count = 0
for i in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(i, LOW, HIGH)
    print("{} guessed in {}".format(i, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1
print("I guessed without being told {}. Max {} guesses".format(correct_count, max_guesses))
