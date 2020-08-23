num = -10
iflag = ""
if (num < 0):
    num *= -1
    iflag = "i"
for i in range(1,num):
    if i**2 == num:
        print("Square root is",i)
        break
    elif i**2 > num:
        print("Square root is about :",(i-1),end=iflag)
        break