def sum_eon(n, t):
    sums = 0
    if t == "e":
        for i in range(n):
            if i % 2 == 0:
                sums += i
        return sums
    elif t == "o":
        for i in range(n):
            if i % 2 != 0:
                sums += i
        return sums
    else:
        return -1


value = input("Enter the value of number and weather odd or even: ")
num, st = value.split()
ans = sum_eon(int(num), st)
print(ans)
