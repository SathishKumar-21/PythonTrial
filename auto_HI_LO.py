import random


low, high = map(int, input("Please enter low and high value: ").split())
if (low < high) != 1:
    low, high = high, low
ans = random.randint(low, high)
print("random answer: ", ans)
guesses = 1
guess = None
while guess != ans:
    guess = low + (high - low) // 2
    if guess > ans:
        high = guess - 1
    elif guess < ans:
        low = guess + 1
    elif guess == ans:
        print("I got in {} guesses".format(guesses))
        break
    guesses += 1

print("Computer guess: ", guess)
