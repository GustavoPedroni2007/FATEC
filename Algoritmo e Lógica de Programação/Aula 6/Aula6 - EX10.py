n = int(input("Informe um número inteiro: "))
prim = int(input("Informe o prim: "))
i = 0
a1 = 1
a2 = 0
a3 = 0
while i < n:
    if a3 > prim:
        print(a3)
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    i += 1
