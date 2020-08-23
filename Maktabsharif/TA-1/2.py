
for num in range(2000,3201):
    num_sum = 0
    for d in str(num):
        num_sum += int(d)
    #print(num_sum)
    for i in range(2,num_sum):
        if num_sum % i == 0:
            break
    else:
        print(num)

