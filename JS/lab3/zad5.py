def select(a) -> list:
    if len(a) < 6:
        raise ValueError("List has to be at least 6 elements long")
    l = sorted(a)
    minl = list(reversed(l[0:3]))
    maxl = list(reversed(l[len(l) - 3:len(l)]))
    return minl + maxl


a = [0, 1, -5, 8, 14, 9, 6]
b = select(a)
print(a)
print(b)
