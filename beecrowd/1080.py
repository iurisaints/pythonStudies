lista_num = []
for i in range(100):
    num = int(input())
    lista_num.append(num)
    i += 1

maior = max(lista_num, key=int)
print(maior)
print(lista_num.index(maior)+1)
