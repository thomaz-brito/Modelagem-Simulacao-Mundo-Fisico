#Considere agora o diagrama de um modelo populacional geométrico
#Vamos considerar os seguintes parâmetros para o nosso modelo:
#P(0)=25 onças
#p_n=0,1 onça/onça/mês
#p_m=0,05 onça/onça/mês

#Usando a equação a diferenças do modelo, construa a série temporal da população de onças para 40 meses.
P=list(range(40))
P[0]=25
i=0
while(i<39):
    P[i+1]=P[i]*1.05
    i=i+1
print(P)

#Plote o gráfico de onças em função do tempo
import numpy as np
tempo=np.arange(0,41,1)
print(tempo)
import matplotlib.pyplot as plt
plt.plot( tempo , P , "ro")
plt.xlabel("Tempo")
plt.ylabel("População")
plt.grid()
