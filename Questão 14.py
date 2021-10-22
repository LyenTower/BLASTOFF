frase = str(input("Digite a palavra:")).strip().upper()
palavras = frase.split()
junto =''.join(palavras)
inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
