lower = int(input("Enter the Lower Range:"))
higher = int(input("Enter the Higher Range:"))
num = int(input("Numbers divisible by:"))

list1 = []

for i in range(lower,higher+1):
    if i%num == 0:
        list1.append(i)

print("Numbers divisible by",num,"are: ",list1)
