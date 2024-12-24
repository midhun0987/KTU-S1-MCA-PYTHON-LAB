#1Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle objects by their area.

class Rectangle:
	def __init__(self,length,breadth):
		self.l=length
		self.b=breadth
		
	def area(self):
		return self.l * self.b
		
	def perimeter(self):
		return 2 * (self.l + self.b)

		
	def compare_area(self, other):

        	if self.area() > other.area():
        		return "First rectangle is larger."

        	elif self.area() < other.area():

            		return "Second rectangle is larger."

        	else:
        		return "Both rectangles have the same area."	
        		

rect=Rectangle(int(input("Enter length of the First rectangle:")),int(input("Enter width of the First rectangle:")))

rect1=Rectangle(int(input("Enter length of the Second rectangle:")),int(input("Enter width of the Second rectangle:")))

print("\nDetails of the first rectangle:")
print("Area of rectangle is:", rect.area())
print("Perimeter of rectangle is:", rect.perimeter())

print("\nDetails of the Second rectangle:")
print("Area of rectangle is:", rect1.area())
print("Perimeter of rectangle is:", rect1.perimeter())
print("\nComparison of Two recrangle:" )

result=rect.compare_area(rect1)
print(result)	
