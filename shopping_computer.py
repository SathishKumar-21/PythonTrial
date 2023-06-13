available_list=['keyboard',
                'monitor',
                'speaker',
                'mouse',
                'printer'
                ]
valid_choice = []
for i in range(1,len(available_list)+1):
    valid_choice.append(str(i))
cart_list = []
choice = None
while choice != '0':
    if choice in valid_choice:
        crt = int(choice) - 1
        if available_list[crt] in cart_list:
            print("Removing {} to cart".format(choice))
            cart_list.remove(available_list[crt])
        else:
            print("Adding {} to cart".format(choice))
            cart_list.append(available_list[crt])
        print("Now your list contains these items: {}".format(cart_list))
    else:
        print("please enter a number to select a product from the below list: ")
        for num, value in enumerate(available_list):
            print("{}:\t{}".format(num+1, value))
    choice = input()
print(cart_list)
