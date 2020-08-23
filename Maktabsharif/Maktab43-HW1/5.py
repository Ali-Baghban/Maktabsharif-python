# Q->5
n = 5273927
counter = 0
check = True

while check:
    if n < 10:
        counter += 1
        check = False
    else:
        n /= 10
        counter += 1
print("Number count = ",counter)

