infinite = 0
results = []

while infinite == 0:
    numInsert = input()
    nums = numInsert.split()
    numx = int(nums[0])
    numy = int(nums[1])

    if(numx == numy):
        for result in results:
            print(result)
        exit()
    elif(numx > numy):
        results.append("Decrescente")
    elif(numx < numy):
        results.append("Crescente")
