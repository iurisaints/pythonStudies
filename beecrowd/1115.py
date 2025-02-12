infinity = 0
results = []

while infinity == 0:
    numInsert = input()
    nums = numInsert.split()
    x = int(nums[0])
    y = int(nums[1])
    #info 
    if(x == 0 or y == 0):
        for result in results:
            print(result)
        exit()
    # primeiro quadrante
    elif(x > 0 and y > 0):
        results.append("primeiro")
    #segundo quadrante
    elif(x < 0 and y > 0):
        results.append("segundo")
    #terceiro quadrante
    elif(x < 0 and y < 0):
        results.append("terceiro")
    #quarto quadrante
    elif(x > 0 and y < 0):
        results.append("quarto")
    
