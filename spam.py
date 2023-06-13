menu = [
    ['egg', 'dosa'],
    ['egg', 'idli', 'dosa'],
    ['egg', 'spam'],
    ['egg', 'dosa', 'spam'],
    ['egg', 'dosa', 'spam', 'idli'],
    ['egg', 'dosa', 'spam', 'idli', 'spam', 'chapathi'],
    ['spam', 'dosa', 'spam', 'idli'],
    ['spam', 'dosa', 'spam', 'idli', 'egg'],
]

for index1, v1 in enumerate(menu):
    for index2, v2 in enumerate(v1):
        if v2.casefold() == 'spam':
            del menu[index1][index2]
    print(v1)
print()

for index1, v1 in enumerate(menu):
    for index2, v2 in enumerate(v1):
        if v2.casefold() != 'spam':
            print(menu[index1][index2], end=', ')
    print()

print()

for meal in menu:
    items = ",".join(item for item in meal if item != 'spam')
    print(items)


