def foo(l):
    to_remove = list()
    for i, v in enumerate(l):
        if i % 3 == 0 or v < 0:

            to_remove.append(i)
    for i in list(reversed(sorted(to_remove))):
        del l[i]


a = [1, 2, 3, 5, 8, -1, -2, -3]
print(a)
foo(a)
print(a)
