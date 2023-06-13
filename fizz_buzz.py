from functions import fizz_buzz

# low = 1
# high = 100
# for i in range(low, high + 1):
#     if i % 2 == 0:
#         play = input(":").casefold()
#         if i % 15 == 0 and play == "fizz buzz":
#             continue
#         elif i % 3 == 0 and play == "fizz":
#             continue
#         elif i % 5 == 0 and play == "buzz":
#             continue
#         elif str(i) == play:
#             continue
#         else:
#             print("You loose to say {}".format(fizz_buzz(i)))
#             break
#     elif i % 2 != 0:
#         print(":{}".format(fizz_buzz(i)))
#     elif i == high:
#         print("Congratulations you won the game")
#     else:
#         print("Please enter a valid input")


next_number = 0
while next_number < 100:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    # players_answer = input("Your go: ").casefold()
    players_answer = input("Your go:").casefold()
    if players_answer != correct_answer:
        print("You lose,the correct answer is {}".format(correct_answer))
        break
else:
    print("Well done, you have reached {}".format(next_number-1))
