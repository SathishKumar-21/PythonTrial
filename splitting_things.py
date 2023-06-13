number = "9, 223, 334, 445, 556, 667, 778"
numbers = number.split(", ")
print(numbers)

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
print(numbers)
