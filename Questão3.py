print("Vamos descobrir qual é o menor número")
primeiro = float(input('Escreva o primeiro numero: '))
segundo = float(input('Escreva o segundo numero: '))
terceiro = float(input('Escreva o terceiro numero: '))
menor = primeiro

if segundo < menor:
    menor = segundo

if terceiro < menor:
    menor = terceiro

print("O menor dos três números é o:", menor)
