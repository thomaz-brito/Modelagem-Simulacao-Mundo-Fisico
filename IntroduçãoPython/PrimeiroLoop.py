#Comece declarando uma lista de zeros chamada lista_y com o mesmo tamanho da lista_x e escreva um loop que prencha essa lista com os valores de y=x^2. Em seguida, imprima a lista_y

lista_x=np.arange(0,19,1)
lista_y=[0]*len(lista_x)
i=0
while(i<len(lista_x)):
    lista_y[i]=int(lista_x[i]**2)
    i=i+1
print(lista_y)
