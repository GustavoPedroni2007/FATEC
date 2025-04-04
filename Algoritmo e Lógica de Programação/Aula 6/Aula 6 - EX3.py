a = int(input("Número inteiro: "))
i = 0
while i < a:
    b = float(input())
    if i == 0:
        menor = b
        maior = b
    if b > maior:
        maior = b
    if b < menor:
        menor = b
    i = i + 1
print(f"O maior número {maior}")
print(f"O menor número {menor}")
