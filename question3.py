a = float(input('Enter first side:'))
b = float(input('Enter second side:'))
c = float(input('Enter third side:'))

if a+b>c and b+c>a and a+c>b:
    print()
else:
    print("Sides do not form a triangle")

s = (a + b + c) / 2
yep=(s*(s-a)*(s-b)*(s-c))
area=0
if yep<=0:
    print()
else:
 area += yep ** 0.5

 print('The area of the triangle is %0.2f' %area)
