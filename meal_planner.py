from contents import pantry, recipes


def shopping_item(shopping: dict, item: str, amount: int) -> None:
    # if item in shopping:
    #     shopping[item] += amount
    # else:
    #     shopping[item] = amount
    shopping[item] = shopping.setdefault(item, 0) + amount


shopping_list = {}
display_menu = {}
for index, meal in enumerate(recipes):
    display_menu[str(index + 1)] = meal
choice = None
while choice != "0":
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_menu.items():
        print(f"{key} - {value}")
    choice = input(": ")
    if choice in display_menu:
        selected_item = display_menu[choice]
        print(f"you have selected {selected_item}")
        ingredients = recipes[selected_item]
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"{food_item} ok")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print("you should buy {} of {}".format(quantity_to_buy, food_item))
                shopping_item(shopping_list, food_item, quantity_to_buy)
for items, qnt in sorted(shopping_list.items()):
    print(items, qnt, sep=": ")
