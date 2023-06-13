choice = '-'
while choice != 0:
    if choice in set(range(0,6)):
        print("You have selected: {}".format(choice))
    else:
        print("please select a product to buy from below list:")
        print("1:\tMother Board")
        print("2:\tGraphics Card")
        print("3:\tProcessor")
        print("4:\tCooler")
        print("5:\tRAM")
        print("6:\tSSD/HDD")
        print("0:\tExit")
    choice = int(input(""))