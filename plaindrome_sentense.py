def palindrome_sentence(string):
    sentences = "".join(sen for sen in string if sen.isalnum() != 0)
    return sentences[::-1] == sentences


sentence = input("Enter the sentence you want to check for palindrome: ")
if palindrome_sentence(sentence.casefold()):
    print("The Entered string \"{}\" is a palindrome".format(sentence))
else:
    print("The Entered string \"{}\" is not a palindrome".format(sentence))

# sentence = []
# value = input("Enter the sentence you want to check for palindrome: ")
# for i in value:
#     if i.isalnum():
#         sentence.append(i)
# sentences = ''.join(sentence).casefold()
# reversed_sentence = sentences[::-1]
# if reversed_sentence == sentences:
#     print("The Entered string \"{}\" is a palindrome".format(value))
# else:
#     print("The Entered string \"{}\" is not a palindrome".format(value))
#
