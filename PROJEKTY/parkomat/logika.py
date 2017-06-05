class Licznik:

    def __init__(self,x):
        self._x=x

    def jedenH(self):
        if(self._x>0):
            return 200
        else:
            return 0

    def dwaH(self):
        if(self._x<=60):
            return Licznik.jedenH(self)
        else:
            self._x=self._x-60
            a = self._x // 60
            b = self._x % 60
            if(b>0):
                return Licznik.jedenH(self) + (a+1)*400
            else:
                return Licznik.jedenH(self) + a*400


    def dwaczteryH(self):
        if (self._x <=1440):
            return Licznik.dwaH(self)
        else:
            self._x = self._x - 1440
            a = self._x // 1440
            b = self._x % 1440
            if (b > 0):
                return Licznik.dwaH(self) + (a+1) * 10000
            else:
                return Licznik.dwaH(self) + a * 10000

    def czteryosiemH(self):
        if (self._x <= 2880):
            return Licznik.dwaczteryH(self)
        else:
            a = self._x // 2880
            if (a > 1):
                self._x = self._x - a * 2880
            else:
                self._x = self._x - 2880
            b = self._x % 2880
            return Licznik.dwaczteryH(self) + a * 25000

    def tydzien(self):
        if (self._x <= 10080):
            return Licznik.czteryosiemH(self)
        else:
            a = self._x // 10080
            if (a > 1):
                self._x = self._x - a * 10080
            else:
                self._x = self._x - 10080
            b = self._x % 10080
            return Licznik.czteryosiemH(self) + a * 180000

    def miesiac(self):
        a = self._x // 40320
        b = self._x % 40320
        if(a>1):
            self._x = self._x - a * 40320
        else:
            self._x = self._x - 40320
        if (b > 0):
            return Licznik.tydzien(self) + a * 750000
        else:
            return a * 750000

    def logika(self):
        if(self._x >= 0 and self._x<=60):
            return Licznik.jedenH(self)
        elif(self._x>60 and self._x<=1440):
            return Licznik.dwaH(self)
        elif(self._x>1440 and self._x<=2880):
            return Licznik.dwaczteryH(self)
        elif (self._x>2880 and self._x<=10080):
            return Licznik.czteryosiemH(self)
        elif (self._x>10080 and self._x<=40320):
            return Licznik.tydzien(self)
        elif (self._x>40320):
            return Licznik.miesiac(self)
        else:
            return -1 #błąd
f = open('logika.txt', 'w')
f.write('l.godzin:' + '   ' + 'l.miesiecy:' + '   ' + 'l.tygodni' + '   ' + 'l.48h' + '   ' + 'l.24h' +  '   ' + 'l.kolejnych.godz.' +  '   ' +'l.pierw.godz.' +  '   ' + 'cena: \n')
for i in range(0,1345*60,60):
    l=Licznik(i)
    a=l.logika()
    f.write(str(i//60) + '      ' + str(i//(24*28*60)) + '      ' + str(i//(24*7*60)) + '      ' + str(i//(24*2*60)) + '      ' + str(i//(24*60)) + '      ' +  str((i//60)-i//(24*60))  +  '      ' + str(i//(24*60)+1) +  '      ' + str(a/100) + ' zł \n')