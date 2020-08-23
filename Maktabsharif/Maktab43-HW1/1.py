#Q->1
# Calculate factorial
# using try to avoid failing or crashing in run the program
try:
    n = int(input("Enter a number > "))
    if n > 0 :
        j = 1
        for i in range(1,n+1):
            j *= i
    else:
        j = 0
    print("Factorial  = "+str(j))
except:
    print("An error has occured")