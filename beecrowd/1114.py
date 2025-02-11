infinity = 0
msgs = []

while infinity == 0:
    password = int(input())

    if(password == 2002):
        msgs.append("Acesso Permitido")
        for msg in msgs:
            print(msg)
        exit()
    elif(password != 2002):
        msgs.append("Senha Invalida")
