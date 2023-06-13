pangram = "The quick brown fox jumps over the lazy dog"
print(pangram)

letters = sorted(pangram)
print(letters)

num = [8, 3, 5, 1, 9, 4, 2, 7, 6, 10]
sorted_num = sorted(num)
print(id(num), num)
print(id(sorted_num), sorted_num)

num.sort()
print(id(num), num)
print(sorted(pangram, key=str.casefold))

dup_num = sorted(num, reverse=True)
print(dup_num)

num.insert(3, 'sathish')
print(num)
