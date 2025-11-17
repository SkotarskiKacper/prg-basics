GridSize=10
XOffset=-5
YOffset=5

for Y in range(GridSize+YOffset,-GridSize+YOffset,-1):
    for X in range(-GridSize+XOffset,GridSize+XOffset,1):
        if X**2==Y:
            print("# ",end="")
        elif X==XOffset and Y==YOffset:
            print("C ",end="")
        elif X==0 or Y==0:
            print(". ",end="")
        else:
            print("  ",end="")
    print("")