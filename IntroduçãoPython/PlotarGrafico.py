#Plote o gráfico da função y=x^2 determinada pelas listas

import numpy as np
lista_x=np.arange(0,19,1)
lista_y=[0]*len(lista_x)
i=0
while(i<len(lista_x)):
    lista_y[i]=int(lista_x[i]**2)
    i=i+1
print(lista_y)

import matplotlib.pyplot as plt
plt.plot( lista_x , lista_y )
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
