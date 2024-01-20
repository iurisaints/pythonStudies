a = int(input())
b = int(input())
soma = 0
i = 0
x = 0
y = 0
if(a > b):
    x = b
    y = a
    while x < y:
        if(x+1 < y):
            x += 1
        else:
            x += 0
        if(x%2!=0):
            soma += x
        if(x+1 == y):
            break
else:
    x = a
    y = b    
    while x < y:
        if(x+1 < y):
            x += 1
        if(x%2!=0 & x < y):
            soma += x
        if(x+1 == y):
            break


print(soma)
