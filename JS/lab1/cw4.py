x=int(input("Podaj liczbe: "))
n=0
for i in range(1,x//2,1):
    if x%i == 0:
        n=n+1
    if n > 2:
        print("nie jest liczba pierwsza")
        break
else:
    print("jest liczba pierwsza")
