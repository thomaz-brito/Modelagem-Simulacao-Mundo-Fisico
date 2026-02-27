#Considere agora o diagrama de um modelo logístico
#P(0)=5
#alfa=0,2
#S=200
#Usando a equação a diferenças do modelo, construa a série temporal de onças para 40 meses.
P=list(range(41))
P[0]=5
i=0
while(i<40):
    P[i+1]=P[i] + P[i]*0.2-0.2*P[i]**2/200
    i=i+1

print(P)

#Plote um gráfico do número de onças em função do tempo.
import numpy as np
tempo=np.arange(0,41,1)
print(tempo)
import matplotlib.pyplot as plt
plt.plot( tempo , P , "ro")
plt.xlabel("Tempo")
plt.ylabel("População")
plt.grid()

#
