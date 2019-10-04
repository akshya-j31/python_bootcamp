NumberOfLines = 5

for x in range(NumberOfLines):
    for y in range(x, NumberOfLines):
        print(" ", end ="")
    if x>1:
        for z in range(x):
            print(z+1, end =" ")
        rev = x-1
        while rev>0:
            print(rev, end =" ")
            rev -= 1

    else:   
        for z in range(x+1):
            print(z+1, end =" ")

    print("\n", end ="")
