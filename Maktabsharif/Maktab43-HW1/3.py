#Q->3

n = 6
# increase * with loop
for i in range (1,n+1):
    star = ""
    for j in range(i):
        star += "*"
    print(star, end="\n")
# decrease * with loop
for i in range(n-1,0,-1):
    star = ""
    for j in range(i):
        star += "*"
    print(star, end="\n")
