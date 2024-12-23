 #11.Write lambda functions to find area of square, rectangle and triangle.



area1=lambda a:a*a
area2=lambda l,b:l*b
area3=lambda b,h:0.5*b*h
s=int(input("enter the side of the square"))
print("area of a square is",area1(s))
l=int(input("enter the length of a rectangle"))
b=int(input("enter the breadth of a rectangle "))
print("area of a rectangle is",area2(l,b))
h=int(input("enter the height of a triangle"))
w=int(input("enter the breadth of a triangle "))
print("area of a triangle is",area3(w,h))