from contents import recipes


def my_deepcopy(d: dict) -> dict:
    c = {}
    for i, v in d.items():
        a = v.copy()
        c[i] = a
    return c


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
