import random

highest = 10
ans = random.randint(1, highest)
guess =""  # TODO: Make a change at nest execution
print(ans)
guess = int(input("Please enter a value between 1 and {}: ".format(highest)))

while guess != ans:
    if guess == 0:
        print("Game over")
        break
    elif guess > ans:
        guess = int(input("Please guess Lower: "))
    else:
        guess = int(input("Please guess Higher: "))
else:
    print("Well done you got it ")
