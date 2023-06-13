from contents import pantry, recipes


def shopping_ingredients(ingredient: dict) -> any:
    sh_dict = {}
    for food_item, quantity in ingredient.items():
        quantity_in_pantry = pantry.get(food_item, 0)
        quantity_to_buy = quantity_in_pantry - quantity
        if quantity_to_buy < 0:
            sh_dict[food_item] = quantity_to_buy * -1
    return sh_dict


display_menu = {}
for index, meal in enumerate(recipes):
    display_menu[str(index + 1)] = meal
choice = None
sum_list = []
while True:
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_menu.items():
        print(f"{key} - {value}")
    choice = input(": ")
    if choice in display_menu:
        selected_item = display_menu[choice]
        print(f"you have selected {selected_item}")
        ingredients = recipes[selected_item]
        shopping_dict = shopping_ingredients(ingredients)
        print(f"The items you need to buy for cooking {selected_item}:")
        print("-------------------------")
        for i, v in shopping_dict.items():
            print(i, v, sep=": ")
            sum_list.append([i, v])
        print("-------------------------")
    elif choice == "0":
        final_list = {}
        for i in range(len(sum_list)):
            for j in range(i+1, len(sum_list)):
                if sum_list[i][0] == sum_list[j][0]:
                    final_list[sum_list[i][0]] = sum_list[i][1] + sum_list[j][1]
                else:
                    final_list[sum_list[i][0]] = sum_list[i][1]
        dict(sorted(final_list.items()))
        print("-------------------------")
        print(f"The Ingredients you need are:")
        for i, v in final_list.items():
            print(i, v, sep=": ")
        break
