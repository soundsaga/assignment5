lower = int(input("Enter the Lower Range:"))
higher = int(input("Enter the Higher Range:"))

for i in range(lower,higher+1):
    if i > 1:  
        for j in range (2,i):  
            if (i % j) == 0:  
                break  
        else:  
            print (i)
