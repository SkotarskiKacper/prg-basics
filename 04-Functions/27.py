def Check(String):
    
    if len(String)!=4:
        return False
    
    sum=int(String[0])+int(String[1])+int(String[2])
    remainder=sum%7

    if remainder==int(String[3]):
        return True
    
    return False

print(Check(f"1082"))