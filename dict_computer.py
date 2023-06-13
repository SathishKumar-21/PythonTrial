available_list = {'1': 'keyboard',
                  '2': 'monitor',
                  '3': 'speaker',
                  '4': 'mouse',
                  '5': 'printer',
                  }
# adding dictionary of available_ list into list of card
# choice = '-'
# cart = []
# item = ""
# while choice != '0':
#     if choice in available_list:
#         item = available_list[choice]
#         if item not in cart:
#             print(f"Adding {item}")
#             cart.append(item)
#         else:
#             print(f"Removing {item}")
#             cart.remove(item)
#     else:
#         for i, v in available_list.items():
#             print(i, v, sep=": ")
#         print("0: to finish")
#     choice = input("> ")
# print(cart)

# adding dictionary of available_ list into dictionary of cart
choice = '-'
cart = {}
item = ""
while choice != '0':
    if choice in available_list:
        item = available_list[choice]
        if choice in cart:
            trash = cart.pop(choice)
            print(f"Item {trash} has been removed from {cart}")
        else:
            cart[choice] = item
            print(f"Added {item} to cart: {cart}")
    else:
        for i, v in available_list.items():
            print(i, v, sep=": ")
        print("0: to finish")
    choice = input("> ")
print(cart)
