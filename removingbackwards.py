num = [4, 5, 104, 105, 106, 204, 205, 206, 306, 350, 273, 265, 267, 102, 103, 10, 15]
# num = [4, 5, 104, 105, 106, 204, 205, 206, 273, 265, 267, 102, 103, 10, 15]
# num = [ 104, 105, 106, 204, 205, 206, 306, 350, 273, 265, 267, 102, 103]
print(num)

for index in range(len(num) - 1, -1, -1):
    if num[index] <= 100 or num[index] >= 300:
        del num[index]
print(num)

top_index = len(num) - 1
for index, value in enumerate(reversed(num)):
    if value <= 100 or value >= 300:
        rev_index = top_index - index
        del num[rev_index]
        print(index, value)
print(num)
