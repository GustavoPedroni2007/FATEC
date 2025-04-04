n = float(input("Digite um valor: "))
i = 1
divisor = 0
while i <= n:
    if n % i == 0:
        divisor = divisor + 1
    i = i + 1
if divisor == 2:
    print(f"{n} é um número primo")
else:
    print(f"{n} não é um número primo")
