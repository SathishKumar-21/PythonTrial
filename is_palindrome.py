def is_palindrome(palindrome):
    return palindrome[::-1] == palindrome
    # return reversed(palindrome) == palindrome


Str = input("Enter the String to check palindrome: ")
if is_palindrome(Str.casefold()):
    print("The Entered string \"{}\" is a palindrome".format(Str))
else:
    print("The Entered string \"{}\" is not a palindrome".format(Str))

