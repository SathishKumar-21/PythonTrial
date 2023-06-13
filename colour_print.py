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


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using ANSI sequence to change colour, etc...
    :param text: The text to print.
    :param effects: The effect that need to be applied on the text by using the constants
       defined at the starting of this module
    """
    effects_strings = "".join(effects)
    output_string = "{0}{1}{2}".format(effects_strings, text, RESET)
    print(output_string)


colour_print("Hello, Red", RED)
colour_print("Hello, Red", RED, YELLOW, BOLD)
colour_print("Hello, Red", REVERSE, BOLD, UNDERLINE)
colour_print("Hello, Red", BOLD)
# testing that the colour effect had been reset
# colour_print("This should be in default terminal colour")
# colour_print("Hello, Blue ", BLUE)
# colour_print("Hello, Green ", GREEN)
# colour_print("Hello, Yellow ", YELLOW)
# colour_print("Hello, Magenta ", MAGENTA)
# colour_print("Hello, Cyan ", CYAN)
# colour_print("Hello, White ", WHITE)
# colour_print("Hello, Black ", BLACK)
# colour_print("Hello, Bold ", BOLD)
# colour_print("Hello, Underline ", UNDERLINE)
# colour_print("Hello, Reverse ", REVERSE)



