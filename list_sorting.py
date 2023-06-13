even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
print(odd)
print(even)

even.extend(odd)
print(even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)
