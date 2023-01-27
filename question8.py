list1 = []
e=[]
o=[]
p=[]
n=[]

for i in range(10):
    num = int(input("Enter an integer:"))
    list1.append(num)

for j in list1:
    if j>0:
        p.append(j)
    else:
        n.append(j)
    if j%2==0:
        e.append(j)
    else:
        o.append(j)

def countx(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

print(p,"positive numbers\n")
print(n,"negative numbers\n")
print(e,"even numbers\n")
print(o,"odd numbers\n")

x=int(input("Enter the number you want to know count of:"))
print(countx(list1,x),"times")
