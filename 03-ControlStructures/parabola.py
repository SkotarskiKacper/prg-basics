GridSize=10
XOffset=-5
YOffset=5

def transform(X,Y,Reset):
    
    if Reset:
        XOffset=0
        YOffset=0
        return

    XOffset+=X
    YOffset+=Y
    return

UserInputFunctions={

    8:transform(0,1,False),
    4:transform(-1,0,False),
    2:transform(0,-1,False),
    6:transform(1,0,False),
    5:transform(0,0,True)

}

while True:

    

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

    print(f"C({XOffset},{YOffset})")
    UserInput=""
    while not UserInput in UserInputFunctions:
        UserInput=int(input("Your Input: "))
    UserInputFunctions[UserInput]

