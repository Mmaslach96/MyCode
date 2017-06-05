import datetime
import sys
import tkinter as tk
import pygubu
from tkinter import *
import random

class Keep:
    def __init__(self):
        self._x = 0 #kwota zaplaty
        self._y = '' # data
        self._repeat = 1 #czy dalej kontynuowac
        self._nrr = '' # nr rejestracyjny na paragon
        self._kwota = 0 #sztywna kwota do zapłaty // bo druga mainpulujemy
        self._res = 0 # czy jest reszta
        self._drukpar = 0 #czy drukujemy paragon
        self._uda = 0 #czy udalo sie wydać resztę

    def adx(self,x):
        self._x=x
    def ady(self,y):
        self._y=y
    def adrepeat(self,repeat):
        self._repeat = repeat
    def adnrr(self, nrr):
        self._nrr = nrr
    def adkwota(self, kwota):
        self._kwota = kwota
    def adres(self, res):
        self._res = res
    def addrukpar(self, drukpar):
        self._drukpar = drukpar
    def aduda(self, uda):
        self._uda = uda
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def getrepeat(self):
        return self._repeat
    def getnrr(self):
        return self._nrr
    def getkwota(self):
        return self._kwota
    def getres(self):
        return self._res
    def getdrukpar(self):
        return self._drukpar
    def getuda(self):
        return self._uda

class Moneta:
    def __init__(self, x):
        y = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        if x in y:
            self._x = x
            Moneta.dodaj(self)
    def dodaj(self):
        b.dodaj(self._x)

class Banknot(Moneta):
    def __init__(self, x):
        y = [1000, 2000, 5000, 10000, 20000, 50000]
        if x in y:
            self._x = x
            Moneta.dodaj(self)

class Bank:
    def __init__(self):
        self._bank = []
        self._reszta = []
        self._dreszta = []

    def dodaj(self,x):
        self._bank.append(x)
        self._reszta.append(x)

    def roznica(self):
        return abs(k.getx())

    def stanBanku(self) -> int:
        bal = 0
        for c in self._bank:
            bal += c
        return bal

    def stanReszty(self) -> int:
        bal = 0
        for c in self._reszta:
            bal += c
        return bal

    def stanDreszty(self) -> int:
        bal = 0
        for c in self._dreszta:
            bal += c
        return bal

    def wydajReszte(self):
        self.a=self.roznica()
        self.i=len(self._bank)-1
        self._bank.sort()
        self._dreszta=[]
        while (self.a>0 and self.i>0):
            if(self.a>=self._bank[self.i]):
                self.a=self.a-b._bank[self.i]
                self._dreszta.append(self._bank[self.i])
                self._bank.remove(self._bank[self.i])
            self.i=self.i-1

        if(self.a==0):
            k.aduda(1)
        else:
            k.aduda(0)
    def wypiszReszta(self):
        self.s='|| '
        for i in self._reszta:
            self.s=self.s+str(i/100) + ' zł || '
        return self.s

    def wypiszDreszta(self):
        self.s='|| '
        for i in self._dreszta:
            self.s=self.s+str(i/100) + ' zł || '
        return self.s

class Rejestracja:
    def __init__(self, x):
        self._x=x

    def sprawdz(self):
        if (self._x==""):
            return 0
        else:
            return 1

class Data:
    def __init__(self,x):
        self._x=x

    def getx(self):
        return self._x

    def roznica(self):
        d1 = datetime.datetime.strptime(self._x, "%Y-%m-%d %H:%M")
        d2 = datetime.datetime.strptime(Data.obecnaData(self), "%Y-%m-%d %H:%M")
        if(d1<d2):
            return 0
        else:
            if((d1-d2).days>0):
                return ((d1-d2).seconds/60) + (((d1-d2).days)*60*24)
            else:
                return (d1-d2).seconds /60

    def obecnaData(self):
        self.now = datetime.datetime.now()
        self.now = self.now.strftime("%Y-%m-%d %H:%M")
        return self.now

    def dataWybrana(self):
        now = datetime.datetime.now()
        self.new = now + datetime.timedelta(minutes = Data.getx(self))
        self.new = self.new.strftime("%Y-%m-%d %H:%M")
        return self.new

    def sprawdz(self):
        try:
            datetime.datetime.strptime(self._x, "%Y-%m-%d %H:%M")
        except ValueError:
            return False
        return True

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

class nieresztaUI(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/niereszta.ui')
        self.mainwindow = builder.get_object('Frame_1', master)
        builder.connect_callbacks(self)

    def button(self):
        self.master.destroy()

class braknrUI(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/braknr.ui')
        self.mainwindow = builder.get_object('Frame_1', master)
        builder.connect_callbacks(self)

    def button(self):
        self.master.destroy()

class odrzuconaUI(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/odrzucona.ui')
        self.mainwindow = builder.get_object('Frame_4', master)
        builder.connect_callbacks(self)

    def button(self):
        self.master.destroy()

class przyjetaUI(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/przyjeta.ui')
        self.mainwindow = builder.get_object('Frame_4', master)
        builder.connect_callbacks(self)

    def button(self):
        self.master.destroy()

class resztaAnulacja(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/resztaanulacja.ui')
        self.mainwindow = builder.get_object('Frame_1', master)
        builder.connect_callbacks(self)
        self.builder.tkvariables['label1'].set('Reszta do wydania: ' + b.wypiszReszta())

    def button(self):
        self.master.destroy()

class resztaNormalna(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/resztanormalna.ui')
        self.mainwindow = builder.get_object('Frame_1', master)
        builder.connect_callbacks(self)
        self.builder.tkvariables['label'].set('Reszta do wydania ('+ str(b.stanDreszty()/100)+ 'zł )' + b.wypiszDreszta())

    def button(self):
        self.master.destroy()

class paymentUI(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/payment.ui')
        self.mainwindow = builder.get_object('Frame_2', master)
        builder.connect_callbacks(self)
        self.kasa=str(k.getx()/100)+' zł'
        self.builder.tkvariables['entry1_var'].set(self.kasa)

    def gr1(self):
        xd=Moneta(1)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-1)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def gr2(self):
        xd = Moneta(2)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-2)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def gr5(self):
        xd = Moneta(5)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-5)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def gr10(self):
        xd = Moneta(10)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-10)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def gr20(self):
        xd = Moneta(20)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-20)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def gr50(self):
        xd = Moneta(50)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-50)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl1(self):
        xd = Moneta(100)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-100)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl2(self):
        xd = Moneta(200)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-200)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl5(self):
        xd = Moneta(500)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-500)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl10(self):
        xd = Banknot(1000)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-1000)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl20(self):
        xd = Banknot(2000)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-2000)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl50(self):
        xd = Banknot(5000)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-5000)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl100(self):
        xd = Banknot(10000)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-10000)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl200(self):
        xd = Banknot(20000)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-20000)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')
    def zl500(self):
        xd = Banknot(50000)
        a=str(b.stanReszty()/100)+' zł'
        self.builder.tkvariables['entry2_var'].set(a)
        k.adx(k.getx()-50000)
        self.builder.tkvariables['entry1_var'].set(str(k.getx()/100)+' zł')

    def plac(self):
        if(k.getx()>0): #1.przypadek gdy jest za mało kasy wyskocz okienko zeby dodac money
            root1= tk.Tk()
            app1=zamaloUI(root1)
            app1.master.title("Dopłać!")
            root1.mainloop()
        elif(k.getx()==0): #2.przypadek gdy jest idealnie kasy na 0 drukuj paragon
            k.adres(0)
            k.addrukpar(1)
            self.master.destroy()
        else: #3. przypadek gdy za dużo kasy wydaje reszte
            b.wydajReszte()
            if(k.getuda()==1): #udalo sie wydac reszte
                k.adres(1)
                k.addrukpar(1) #drukuj b._dreszta
                self.master.destroy()
            else: #komunikat o bledzie ze nie udalo sie wydac reszty
                k.addrukpar(0)
                k.adres(2)
                self.master.destroy()
                root1 = tk.Tk()
                app1 = nieresztaUI(root1)
                app1.master.title("Bład!")
                root1.mainloop()

    def anuluj(self):
        k.addrukpar(0)
        if(len(b._reszta)==0): #przypadek gdy nic kasy nie wlozyl
            k.adrepeat(1)
            k.adres(0)
        else:
            k.adres(2) # dwojka czy reszta zwraca all z reszty
            k.adrepeat(1)
            for c in b._reszta:
                b._bank.remove(c)
        self.master.destroy()

    def karta(self):
        if (len(b._reszta) > 0): #jeśli wrzucił coś kasy ale jednak płaci kartą
            for c in b._reszta:
                b._bank.remove(c)
            k.adres(2)
        self.a=random.randint(0, 100)
        if(self.a>=1):
            self.master.destroy()
            k.adrepeat(1)
            k.addrukpar(1)
            root1=tk.Tk()
            app1=przyjetaUI(root1)
            app1.master.title("Zapłacono")
            root1.mainloop()
        else:
            self.master.destroy()
            k.adrepeat(1)
            k.addrukpar(0)
            root3=tk.Tk()
            app3=odrzuconaUI(root3)
            app3.master.title("Błąd")
            root3.mainloop()

class guiUI(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/gui.ui')
        self.mainwindow = builder.get_object('Frame_1', master)
        builder.connect_callbacks(self)
        #data
        self.builder.tkvariables['entry2_var'].set(Data.obecnaData(self))

    def button1(self):
        self.y=self.builder.tkvariables['entry2_var'].get()
        a=Data(self.y)
        if not a.sprawdz():
            root1= tk.Tk()
            app1=braknrUI(root1)
            app1.master.title("Błąd")
            root1.mainloop()
            return
        self.x=a.roznica()

        min = a.roznica()
        l = Licznik(min)
        c=l.logika()
        s=''
        s=str(c/100) + ' zł'
        self.builder.tkvariables['entry3_var'].set(s)


    def button2(self):
        self.y=self.builder.tkvariables['entry2_var'].get()
        a=Data(self.y)
        if not a.sprawdz():
            root1= tk.Tk()
            app1=braknrUI(root1)
            app1.master.title("Błąd")
            root1.mainloop()
            return
        self.x=a.roznica()

        min = a.roznica()
        l = Licznik(min)
        self.c=l.logika()
        s=''
        s=str(self.c/100) + ' zł'
        self.builder.tkvariables['entry3_var'].set(s)

        r = Rejestracja(self.builder.tkvariables['entry1_var'].get())
        self.r1=self.builder.tkvariables['entry1_var'].get()
        if (r.sprawdz() == 1 and self.c>0):
            k.adx(self.c)
            k.ady(self.y)
            k.adnrr(self.r1)
            k.adkwota(self.c)
            self.master.destroy()
        else:
            root1= tk.Tk()
            app1=braknrUI(root1)
            app1.master.title("Błąd")
            root1.mainloop()

class zamaloUI(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/zamalo.ui')
        self.mainwindow = builder.get_object('Frame_2', master)
        builder.connect_callbacks(self)

    def button(self):
        self.master.destroy()

class paragonUI(pygubu.TkApplication):
    def __init__(self, master):

        # TKinter/pygubu
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui/paragon.ui')
        self.mainwindow = builder.get_object('Frame_1', master)
        builder.connect_callbacks(self)
        self.builder.tkvariables['label1'].set(k.getnrr())
        self.builder.tkvariables['label2'].set(str(k.getkwota()/100) + ' zł')
        self.builder.tkvariables['label3'].set(k.gety())

    def button(self):
        self.master.destroy()

if __name__ == '__main__':
    k = Keep()
    b = Bank()

    def main():
        root = tk.Tk()
        app = guiUI(root)
        app.master.title("Parkomat")
        root.mainloop()
    def pay():
        root1 = tk.Tk()
        app1 = paymentUI(root1)
        app1.master.title("Pay")
        root1.mainloop()
    def reszta():
        root2 = tk.Tk()
        app2 = resztaAnulacja(root2)
        app2.master.title("Reszta")
        root2.mainloop()
    def resztanorm():
        root2 = tk.Tk()
        app2 = resztaNormalna(root2)
        app2.master.title("Reszta")
        root2.mainloop()
    def paragon():
        root3 = tk.Tk()
        app3 = paragonUI(root3)
        app3.master.title("Paragon")
        root3.mainloop()


    b._bank = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 50000, 100000, 200000, 500000]  # ustawiamy monety do wydania
    while(k.getrepeat()==1): # jesli powtorka jest rowna 1 to leci od nowa
        b._reszta = [] # zerujemy saldo
        k.adx(0) # zerujemy do zapłacenia
        main() #odpalamy maina
        k.adrepeat(0) #dajemy 0 żeby w razie offniecia okienka wyłaczyć apke
        if (k.getx() > 0): #jeśli zapłata jest większa od 0 to przechodzimy do płacenia
            pay() #placenie ui
            if(k.getres()==1): #wydaje normalnie reszte
                resztanorm()
            elif(k.getres()==2): #wydaje reszte w przypadku anulacji
                reszta()
            else: #wraca do menu
                k.adrepeat(1)

            if(k.getdrukpar()==1): # czy zaplacone i drukowac
                paragon()
                k.adrepeat(1)
            else:
                k.adrepeat(1)

#wyjątek z złą datą



