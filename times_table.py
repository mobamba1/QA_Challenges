number = int(input("Times table"))

def multiple(number,i):
    
    list = []
    iteration = 1
    while iteration < number + 1:
        
        addtolist = iteration * i
        list.append(addtolist)
        iteration += 1




    return list

for i  in range(1,number + 1):
    print(multiple(number, i))


for x in range (1, number + 1):
    for y in range (1, number + 1):
        print ('{:3}'.format(x*y), end=' ')
    print()






  