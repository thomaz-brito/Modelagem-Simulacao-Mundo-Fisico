#Agora, vamos aplicar os conhecimentos adquiridos nos itens anteriores nos três principais modelos de crescimento populacional que vimos em aula.
#Vamos considerar os seguintes parâmetros para o nosso modelo:
#P(0) =15 [onças]
#N=4 [nascimentos de onças/mês] 
#M=1[mortes de onças/mês]

P=list(range(40))
P[0]=15
i=0
while(i<39):
    P[i+1]=P[i]+4-1
    i=i+1

print(P)

#Em seguida, plote um gráfico do número de onças em função do tempo.
import numpy as np
tempo=np.arange(1,41,1)
import matplotlib.pyplot as plt
plt.plot( tempo , P )
plt.xlabel("Tempo")
plt.ylabel("População")
plt.grid()
