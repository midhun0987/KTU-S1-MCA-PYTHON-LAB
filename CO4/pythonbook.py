#5.Create a class Publisher (name). Derive class Book from Publisher with attributes title and author. Derive class Python from Book with attributes price and no_of_pages. Write	a program that displays information about a Python book. Use base class constructor invocation and method overriding.

#Date:5-12-24

class Publisher:
	def __init__(self,name):
		self.name=name
	def display():
		pass
		
		
class Book(Publisher):
	def __init__(self,name,title,author):
		super().__init__(name)
		self.title=title
		self.author=author
	def display():
		pass
		
		
class Python(Book):
	def __init__(self,name,title,author,price,no_of_pages):
		super().__init__(name,title,author)
		self.price=price
		self.no_of_pages = no_of_pages
	
	def display(self):
		print("Book details:")
		print("Name of Title:",self.title)
		print("Name of author:",self.author)
		print("Name of publisher:",self.name)
		print("Price of boooks:",self.price)
		print("Number of pages:",self.no_of_pages)
		

book1=Python(input("Enter the titile of book"),input("Enter name of Author:"),input("Enter name of publisher:"),int(input("Enter price of Book:")),int(input("Number of pages in book")))	

book1.display()	

		
