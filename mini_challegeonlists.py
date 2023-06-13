choice = '-'
computer_parts= []

while choice != 0:
    if choice in range(1, 7):
        print("Adding {} to the list".format(choice))
    if choice == 1:
        computer_parts.append("computer")
    elif choice == 2:
        computer_parts.append("monitor")
    elif choice == 3:
        computer_parts.append("keyboard")
    elif choice == 4:
        computer_parts.append("mouse")
    elif choice == 5:
        computer_parts.append("mouse mat")
    elif choice == 6:
        computer_parts.append("HDMI")
    else:
        print("Please enter the number of the item to add it into the list:")
        print("1:\tcomputer")
        print("2:\tmonitor")
        print("3:\tkeyboard")
        print("4:\tmouse")
        print("5:\tmouse mat")
        print("6:\tHDMI")
        print("0:\texit")

    choice = int(input())
print(computer_parts)

