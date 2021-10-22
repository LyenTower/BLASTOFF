print("Vamos construir a tabuada de um determinado número n")

a = int(input("Escreva o número que você deseja obter a tabuada:"))

for n in range(0, 11):
    print("{} x {} = {}".format(a, n, a*n))

