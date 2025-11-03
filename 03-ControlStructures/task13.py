NumberToCheck=input("Enter EAN-13 article number ")

if len(NumberToCheck)==13 and NumberToCheck[0:3]=="590":
    print("Number ok")
else:
    print("number not ok")