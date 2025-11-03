number_table=[]
less_than=100

#Resetting the table
for n in range(less_than):
    number_table.append(True)

for n in range(int(less_than/2)):
    i=0
    while i*n<less_than:
        number_table[i*n]=False
        i+=1

for i in range(len(number_table)):
    if number_table[i]:
        print(i)