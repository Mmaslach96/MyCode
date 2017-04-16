def printCenter(tekst, szerokosc = 50):
    x = len(tekst)
    y = int((szerokosc - x) / 2)
    print(" " * y, tekst, " " * y)

printCenter("Zażółć gęślą jaźń")
printCenter("Zażółć gęślą jaźń", 70)
