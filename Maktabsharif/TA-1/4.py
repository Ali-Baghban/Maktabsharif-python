for row in range(1,10):
    print("\t"*(row-1),end="")
    for column in range(1,10):
        if column>= row:
            print(row*column,end="\t")
    print("\n")