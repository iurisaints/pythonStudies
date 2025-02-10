testes = int(input())
i = 0
somas = []

while i < testes:
    numInsert = input()
    nums = numInsert.split()
    a = int(nums[0])
    b = int(nums[1])
    
    if a > b:
        a, b = b, a  # Garantir que a seja sempre menor que b
    
    soma_impares = 0
    for num in range(a + 1, b):
        if num % 2 != 0:
            soma_impares += num
    
    somas.append(soma_impares)
    i += 1

for soma in somas:
    print(soma)
