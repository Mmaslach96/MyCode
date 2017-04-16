# import modułów
import numpy as np
import matplotlib.pyplot as plt

from fuzzython.fsets.triangular import Triangular
from fuzzython.adjective import Adjective
from fuzzython.variable import Variable

from fuzzython.fsets.triangular import Triangular
from fuzzython.adjective import Adjective
from fuzzython.variable import Variable

#Definicja zmiennych lingwistycznych
#Dla każdej ze zmiennych definiujemy wartości lingwistyczne, trójkątne zbiory rozmyte

#procesor
p_poor = Triangular((-1,0), (500,1), (900,0))
p_average = Triangular((500,0), (900,1), (1500,0))
p_good = Triangular((900,0), (1500,1), (2500,0))
p_poor = Adjective('p_poor', p_poor)
p_average = Adjective('p_average', p_average)
p_good = Adjective('p_good', p_good)
procesor = Variable('procesor', 'star', p_poor, p_average, p_good)

#karta graficzna
k_poor = Triangular((-1,0), (350,1), (700,0))
k_average = Triangular((350,0), (700,1), (1200,0))
k_good = Triangular((700,0), (1200,1), (1900,0))
k_poor = Adjective('k_poor', k_poor)
k_average = Adjective('k_average', k_average)
k_good = Adjective('k_good', k_good)
karta = Variable('karta', 'star', k_poor, k_average, k_good)

#moc komputera w %%%%
m_low = Triangular((-1,0), (1,1), (50,0))
m_medium = Triangular((0,0), (50,1), (100,0))
m_high = Triangular((50,0), (100,1), (101,0))
m_low = Adjective('t_low', m_low)
m_medium = Adjective('t_medium', m_medium)
m_high = Adjective('t_high', m_high)
moc = Variable('moc', '%', m_low, m_medium, m_high, defuzzification='COG', default=0)

# Definicja reguł
from fuzzython.ruleblock import RuleBlock

scope = locals()

rule1 = 'if procesor is p_poor or karta is k_poor then moc is m_low'
rule2 = 'if procesor is p_average then moc is m_medium'
rule3 = 'if procesor is p_good or karta is k_good then moc is m_high'

block = RuleBlock('first', operators=('MIN','MAX','ZADEH'), activation='MIN', accumulation='MAX')
block.add_rules(rule1, rule2, rule3, scope=scope)


# Stworzenie sterownika rozmytego typu Mamdani
from fuzzython.systems.mamdani import MamdaniSystem

mamdani = MamdaniSystem('ms1', block)

# wnioskowanie
inputs = {'procesor': 2000, 'karta': 1800}
res = mamdani.compute(inputs)
print(res)

sampled = np.linspace(0, 10, 20)
x, y = np.meshgrid(sampled, sampled)
z = np.zeros((len(sampled),len(sampled)))

for i in range(len(sampled)):
    for j in range(len(sampled)):
        inputs = {'procesor': x[i, j], 'karta': y[i, j]}
        res = mamdani.compute(inputs)
        z[i, j] = res['first']['moc']

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                       linewidth=0.4, antialiased=True)

cset = ax.contourf(x, y, z, zdir='z', offset= -1, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset= 11, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset= 11, cmap='viridis', alpha=0.5)

ax.view_init(100, 2500)
plt.show()