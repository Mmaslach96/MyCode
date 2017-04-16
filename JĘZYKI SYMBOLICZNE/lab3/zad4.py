a=[3,1,2,0,4]
b=[3,12,32,2,4]

def f(a,b):
    c=[a[i]+b[i] for i in range(min(len(a),len(b)))]
    print(c[ : ])

f(a,b)
