#y=int(input("Podaj liczbe: "))

def f(x):
    n=0
    for i in range(1,x//2,1):
        if x%i == 0:
            n=n+1
        if n > 2:
            print("nie jest liczba pierwsza")
            break
    else:
        print("jest liczba pierwsza")

def funkcja():
    for i in range(30):
        x=(2**i)-1
        print("Dla p=",i," liczba Mersenne'a: ",x)
        f(x)
        print("")

funkcja()

        
