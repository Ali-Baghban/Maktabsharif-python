# Q->4

a = 20
b = 23

for i in range(a,b):
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)
        break
else:
    print("There's no prime number in the range")