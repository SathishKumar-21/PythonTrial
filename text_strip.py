# jabber = open("Jabberwocky.txt", "r")
#
# for line in jabber:
#     print(line.rstrip())
#     print(len(line))
#
# jabber.close()
with open('Jabberwocky.txt') as jabber:
    line = jabber.readlines()
# print(line)
# print("*" * 80)
# print(line[-4:])
# for i in line:
#     print(i)
char = "'Twas br"
char1 = "toves"

no_twas = line[0].strip()
print(no_twas.lstrip(char))
print(no_twas.rstrip(char1))
