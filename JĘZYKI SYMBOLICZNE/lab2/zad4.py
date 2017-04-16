import random
def k4():
    return random.randint(1,4)
def k8():
    return random.randint(1,8)
def k10():
    return random.randint(1,10)
def k20():
    return random.randint(1,20)

def rollDice(f):
    liczby=f.split("k")
    a=int(liczby[0])
    b=int(liczby[1])
    if(a>b):
        c=a
        a=b
        b=c
    return(random.randint(a,b))


