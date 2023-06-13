lists = ["computer", "monitor", "mouse", "keyboard", "printer", "speaker"]
print(lists)
choice = '-'

choice = input("Enter the device you need to find: ")
pos = lists.index(choice)
print("your item is in {} position of the list".format(pos))
print("The first letter of the item is: {}".format(lists[pos][0::2]))




