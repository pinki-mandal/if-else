    
x=int(input("enter the first side"))
y=int(input("enter the second side"))
z=int(input("enter the third side"))
if x==y==z:
    print("equilateral triangle")
elif x==y or y==z or z==x :
    print("isosceles triangle")  
else:
    print("scalene triangle")     


