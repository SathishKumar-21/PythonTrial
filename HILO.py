high = 1000
low = 1
print("Please guess a number between {} and {}: ".format(low, high))
input("Press Enter to start the game")
guesses = 1
while True:
    guess = low + (high - low) // 2
    HI_LO = input("My guess is {}, Should i guess higher or lower."
                  "Enter h for high and l for low or c ,if i was correct: "
                  .format(guess).casefold())
    if HI_LO == "h":
        low = guess + 1
    elif HI_LO == "l":
        high = guess - 1
    elif HI_LO == "c":
        print("I got in {} guesses".format(guesses))
        break
    else:
        print("Please enter h or l or c: ")
    guesses += 1
