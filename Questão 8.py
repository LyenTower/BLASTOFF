print("Descobrindo se o número é primo ou não.")
x = int(input("Escreva aqui o número: "))
total = 0
for c in range(1, x + 1):
    if x % c == 0:
        total += 1

if total == 2:
    print("{} é primo.".format(x))
else:
    print("{} não é primo.".format(x))