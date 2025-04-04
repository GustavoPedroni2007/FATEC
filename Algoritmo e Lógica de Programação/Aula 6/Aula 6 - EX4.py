a = int(input("Número inteiro: "))
i = 0
while i < a:
    b = float(input(f"Digite o {i + 1}º Elemento: "))
    if b > 0:
        if i == 0 or b > maior:
            maior = b
        if i == 0 or b < menor:
            menor = b
        i = i + 1
    else:
        print("Número Invalido")
print(f"O maior número {maior}")
print(f"O menor número {menor}")
