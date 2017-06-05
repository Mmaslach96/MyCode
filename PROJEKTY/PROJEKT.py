import datetime

class Moneta:
    def __init__(self, x):
        y = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        if x not in y:
            x = 0
        self._x = x

    def wypisz(self):
        print(self._x)

    def get_x(self) -> int:
        return self._x

class Banknot(Moneta):
    def __init__(self,x):
        y = [1000,2000,5000,10000,20000,500000]
        if x not in y:
            x = 0
        self._x = x

class Data:
    def __init__(self,x):
        self._x=x

    def getx(self):
        return self._x

    def obecnaData(self):
        self.now = datetime.datetime.now()
        self.now = self.now.strftime("%Y-%m-%d %H:%M")
        return self.now

    def dataWybrana(self):
        now = datetime.datetime.now()
        self.new = now + datetime.timedelta(minutes = Data.getx(self))
        self.new = self.new.strftime("%Y-%m-%d %H:%M")
        return self.new

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
            b = self._x % 60 >0
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
            b = self._x % 1440 > 0
            if (b > 0):
                return Licznik.dwaH(self) + (a + 1) * 10000
            else:
                return Licznik.dwaH(self) + a * 10000

    def czteryosiemH(self):
        if (self._x <= 2880):
            return Licznik.dwaczteryH(self)
        else:
            self._x = self._x - 2880
            a = self._x // 2880
            b = self._x % 2880 > 0
            if (b > 0):
                return Licznik.dwaczteryH(self) + (a + 1) * 25000
            else:
                return Licznik.dwaczteryH(self) + a * 25000

    def tydzien(self):
        if (self._x <= 10080):
            return Licznik.czteryosiemH(self)
        else:
            self._x = self._x - 10080
            a = self._x // 10080
            b = self._x % 10080 > 0
            if (b > 0):
                return Licznik.czteryosiemH(self) + (a + 1) * 180000
            else:
                return Licznik.czteryosiemH(self) + a * 180000

    def miesiac(self):
        self._x = self._x - 40320
        a = self._x // 40320
        b = self._x % 40320 > 0
        if (b > 0):
            return Licznik.tydzien(self) + (a + 1) * 750000
        else:
            return Licznik.tydzien(self) + a * 750000

    def logika(self):
        if(self._x >= 0 and self._x<=60):
            return Licznik.jedenH(self)
        elif(self._x>60 and self._x<=1440):
            return Licznik.dwaH(self)
        elif(self._x>1440 and self._x<=2880):
            return Licznik.dwaczteryH(self)
        elif (self._x>2880 and self._x<=10080):
            return Licznik.czteryosiemH(self)
        elif (self._x>=10080 and self._x<=40320):
            return Licznik.tydzien(self)
        elif (self._x>40320):
            return Licznik.miesiac(self)
        else:
            return -1 #błąd






a=Licznik(2880+121)
print(a.logika())

