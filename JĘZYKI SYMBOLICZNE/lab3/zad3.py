a=[3,1,2,0,4]

def f(a):
    b = [i for i in a]
    for i, v in enumerate(b):  
        if 0 < i < (len(a) - 1):
            b[i] = (a[i - 1] + a[i] + a[i + 1]) / 3
    print(b[ : ])

f(a)

