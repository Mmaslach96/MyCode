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

q_poor = Triangular((-0.1,0), (2,1), (3,0))
q_average = Triangular((0,0), (7,1), (10,0))
q_good = Triangular((8,0), (10,1), (11,0))
q_poor = Adjective('q_poor', q_poor)
q_average = Adjective('q_average', q_average)
q_good = Adjective('q_good', q_good)
quality = Variable('quality', 'star', q_poor, q_average, q_good) #jakość jedzenia w skali od 0 do 10

s_poor = Triangular((-0.1,0), (4,1), (5,0))
s_average = Triangular((0,0), (8,1), (10,0))
s_good = Triangular((5,0), (1,1), (10.1,0))
s_poor = Adjective('s_poor', s_poor)
s_average = Adjective('s_average', s_average)
s_good = Adjective('s_good', s_good)
service = Variable('service', 'star', s_poor, s_average, s_good) #obsługa w skali od 0 do 10

t_low = Triangular((-0.1,0), (0,1), (13,0))
t_medium = Triangular((0,0), (13,1), (25,0))
t_high = Triangular((13,0), (25,1), (25.1,0))
t_low = Adjective('t_low', t_low)
t_medium = Adjective('t_medium', t_medium)
t_high = Adjective('t_high', t_high)
tip = Variable('tip', '%', t_low, t_medium, t_high, defuzzification='COG', default=0) # napiwek od 0 do 25%

# Definicja reguł
from fuzzython.ruleblock import RuleBlock

scope = locals()

rule1 = 'if quality is q_poor and service is s_poor then tip is t_low' #tutej zamieniamy na and
rule2 = 'if quality is q_average then tip is t_medium'
rule3 = 'if quality is q_good or service is s_good then tip is t_high' #tutej zamieniamy na and

block = RuleBlock('first', operators=('MIN','MAX','ZADEH'), activation='MIN', accumulation='MAX')
block.add_rules(rule1, rule2, rule3, scope=scope)


# Stworzenie sterownika rozmytego typu Mamdani
from fuzzython.systems.mamdani import MamdaniSystem

mamdani = MamdaniSystem('ms1', block)

# wnioskowanie
inputs = {'quality': 6.5, 'service': 9.8}
res = mamdani.compute(inputs)
print(res)

sampled = np.linspace(0, 10, 20)
x, y = np.meshgrid(sampled, sampled)
z = np.zeros((len(sampled),len(sampled)))

for i in range(len(sampled)):
    for j in range(len(sampled)):
        inputs = {'quality': x[i, j], 'service': y[i, j]}
        res = mamdani.compute(inputs)
        z[i, j] = res['first']['tip']

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                       linewidth=0.4, antialiased=True)

cset = ax.contourf(x, y, z, zdir='z', offset= -1, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset= 11, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset= 11, cmap='viridis', alpha=0.5)

ax.view_init(30, 200)
plt.show()