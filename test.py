import random

highest = 10
ans = random.randint(1, highest)
guess =""  # TODO: Make a change at nest execution
print(ans)
guess = int(input("Please enter a value between 1 and {}: ".format(highest)))

for i in range(5):
    if guess == ans and i == 0:
        print("Well done you got it in the first time")
        break
    if guess == 0:
        print("Game over")
        break
    elif guess > ans:
        guess = int(input("Please guess Lower: "))
    elif guess < ans:
        guess = int(input("Please guess Higher: "))
    elif guess == ans:
        print("Finally you got it")
        break
else:
    print("sorry")
