def is_palindrome(string: str) -> bool:
    """
    palindrome is a string that reads the same forwards as backwards.
    :param string: The `string` to check
    :return: True if `string` is a palindrome or false otherwise
    """
    return string[::-1] == string


def palindrome_sentence(string: str) -> bool:
    """
    Used to check weather a sentence is palindrome or not palindrome.
    palindrome is a string that reads the same forwards as backwards.
    :param string: The string `sentence` to check
    :return: True if `string of sentence` is a palindrome or false otherwise
    """
    sentences = "".join(sen for sen in string if sen.isalnum() != 0)
    return sentences[::-1] == sentences


def fibonacci(n: int) -> int:
    """
    This function returns the `n` th fibonacci number for the positive integer `n`.
    :param n: the positive integer value.
    :return: Returns the fibonacci number of integer `n`.
    """
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


def banner(text: str = " ", space_width: int = 80) -> None:
    """
    This function creates a banner with the text you have given and followed by the required space width.
    :param text: parameter that takes the string to be printed inside the banner
    :param space_width: parameter that takes the space width for the banner.
    """
    if len(text) > space_width - 4:
        raise ValueError("Error occurred")
    elif text == "*":
        print("*" * space_width)
    else:
        print("**{}**".format(text.center(space_width - 4)))


# Some ANSI escape sequence for colour and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, effect: str = RESET) -> None:
    """
    Print `text` using ANSI sequence to change colour, etc...
    :param text: The text to print.
    :param effect: The effect that need to be applied on the text by using the constants
       defined at the starting of this module
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


def guess_binary(answer: int, low: int, high: int) -> int:
    """
    This function returns the number of guesses of an integer that passes as answer by binary searching method.
    :param answer: The value needed to find in this guess function
    :param low: lower limit
    :param high: higher limit
    :return: `int` value of guess number made to find the answer in the given limit
    """
    guesses = 1
    while True:
        guess = low + (high - low) // 2
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        elif guess == answer:
            return guesses
        guesses += 1


def fizz_buzz(n: int) -> str:
    """
    This function represents a mathematical game `fizz buzz`.
    :param n: The `int` value to be passed into the game
    :return: It returns fizz if the integer `n` is dividable by 3.
        It returns buzz if the integer `n` is dividable by 5. It returns fizz buzz if the integer `n` is
        dividable by both 3 and 5.
    """
    if n % 15 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


