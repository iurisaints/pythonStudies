a = 1
b = 60
for i in range(13):
    if i == 0:
        print("I=1 J=60")
    else:
        ka = i * 3
        kb = i * 5
        print("I=%s J=%s" % (a+ka, b-kb))
