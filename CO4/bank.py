#2..Create a Bank account with members account number, name, type of account and balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
Date:5-12-2024


class Bank:
	def __init__(self,acc_no,name,acc_type,balance):
		self.ano=acc_no 
		self.anname=name
		self.atype=acc_type
		self.abalance=balance
		
	def deposit(self,amt):
		if amt>0:
			self.abalance=self.abalance+amt
			print("Amount deposited successfully")
		else:
			print("Invalid amount")
			
	def withdraw(self,amt):
		if amt > self.abalance:
			print("Insufficient balance.")
		else:
			print("Amount succesfully withdrawn")
			self.abalance -= amount
                	
	def displaydetails(self):
		print("Name:", self.anname)
		print("Account No:", self.ano)
		print("Account Type:", self.atype)
		print("Balance Amount:", self.abalance)		
           	 	
          	

account=int(input("Enter account number:"))
name=input("Enter name:")
acc_type=input("Enter account type(Fixed or savings):")
balance=int(input("Enter current savings:"))

account = Bank(account,name,acc_type, balance)

while(True):
	  print("\n.......MENU.......\n1.Deposit\n2.Withdraw\n3.Display Account Info\n4.Exit")
	  choice = int(input("Enter your choice: "))
	  
	  if choice == 1:
	  	amount = int(input("Enter amount to deposit: "))
	  	account.deposit(amount)
	  elif choice == 2:
	  	amount = int(input("Enter amount to withdraw: "))
	  	account.withdraw(amount)
	  elif choice == 3:
	  	account.displaydetails()
	  elif choice == 4:
	  	print("Exiting the program.")
	  	
	  	break
	  else:
	  	print("Invalid choice. Please try again.")

	
	

		
		
		
		
		
		
		
		
		
