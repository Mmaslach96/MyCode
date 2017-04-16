def f(f,xp=-1,xk=1,lp=10):
      for i in range(xp*10,xk*10,2):
          print(i,"  ",f(i))

f(lambda i: 2*i)

