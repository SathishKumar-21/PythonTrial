num = [4, 5, 104, 105, 106, 204, 205, 206, 306, 350]
print(num)

mini = 100
maxi = 300
stop = 0
for index, value in enumerate(num):
    if value >= mini:
        stop = index
        break
# Type 1: fast and efficient only works on sorted list
print(stop)
del num[:stop]
print(num)

start = 0
for index in range(len(num)-1, 5, -1):
    if num[index] <= maxi:
        start = index + 1
        break

print(start)
del num[start:]
print(num)

# Type 2: medium and efficient works on both sorted list and unsorted list
top_index = len(num) - 1
for index, value in enumerate(reversed(num)):
    if value <= 100 or value >= 300:
        rev_index = top_index - index
        del num[rev_index]
print(num)

# Type 3: slow and efficient works on both sorted list and unsorted list
for index in range(len(num) - 1, -1, -1):
    if num[index] <= 100 or num[index] >= 300:
        del num[index]
print(num)




