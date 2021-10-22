print(('Um número é múltiplo do outro?'))

a = float(input("Escreva o primeiro número:"))
b = float(input("Escreva o segundo número:"))

a1 = a % b
a2 = b % a

if a1 == 0 or a2 == 0:
    print("{} e {} são múltiplos".format(a, b))
else:
    print("{} e {} não são múltiplos".format(a, b))
