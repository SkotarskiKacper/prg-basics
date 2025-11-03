GridSize=20


for Y in range(GridSize):
    for X in range(GridSize):
        if X**2==Y:
            print("# ",end="")
            #Row.insert("# ")
        elif X==0 or Y==0:
            print(". ",end="")
            #Row.insert(. ")
        else:
            print("  ",end="")
            #Row.insert("  ")
    print("")