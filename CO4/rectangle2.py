 #3Create a class Rectangle with private attributes length and width. Overload ‘<’ operator to compare the area of 2 rectangles.

#Date:5-12-24


class Rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width=width
	def area(self):
		return self.length*self.width
	def __lt__(self,other):
		return self.area() < other.area()
		
		
rect1=Rectangle(int(input("Enter length of the First rectangle:")),int(input("Enter width of the First rectangle:")))
rect2=Rectangle(int(input("Enter length of the Second rectangle:")),int(input("Enter width of the Second rectangle:")))

print("Area of rectangle 1 is:", rect1.area())
print("Area of rectangle 2 is:", rect2.area())

if rect1<rect2:
	print("Area of rectangle 1 is lesser than area of rectangle 2.")
elif rect1>rect2:
	print("Area of rectangle 1 is greater than area of rectangle 2.")
else:
	print("Both rectangles have same area.")
