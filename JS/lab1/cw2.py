x = int(input("Podaj rok prosze: "))
if x%4 == 0:
    if x%400 == 0:
        print("Rok ten jest przestepny")
    elif x%100 == 0 and x%400 != 0:
        print("Rok ten nie jest przestepny")
    else:
        print("Rok ten jest przestepny")
        
else:
    print("Rok ten nie jest przestepny")

        
