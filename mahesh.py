for i in range(500):
    h = i // 100
    t = (i // 10) % 10
    o = i % 10
    if o == t or o == h:
        s = h+t+o
        if s <= 5:
            print(i)
