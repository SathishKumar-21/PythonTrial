value = input("Enter three value seperated by comas: ")

numbers = value.split(",")
number = []
for i in range(len(numbers)):
    number.append(int(value[i]))
    # numbers[i] = int(numbers[i])

print((number[0]+number[1])-number[2])
