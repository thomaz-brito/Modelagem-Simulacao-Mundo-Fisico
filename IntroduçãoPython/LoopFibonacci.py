#Gere um código que preencha os 100 primeiros termos da sequência de Fibonacci. Imprima a lista de Fibonacci e perceba como os valores crescem de forma acelerada.

fib=[0]*100
fib[0] = 1
fib[1] = 1
i=0
while (i <= 97):
    fib[i+2]=fib[i+1]+fib[i]
    i=i+1

print(fib)
