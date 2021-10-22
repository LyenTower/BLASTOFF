print("Quais são os números pares em um intervalo determinado 1,2,3,...n")

a = int(input("Escreva o número n: "))

for n in range(1, a+1):
    if n % 2 == 0:
        print(n, end=', ')
print("Isso é tudo pessoal!")