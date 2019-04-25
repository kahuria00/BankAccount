class Account:
	def __init__ (self,first_name,second_name,initial_balance):

		self.first_name=first_name
		self.second_name=second_name
		self.initial_balance=initial_balance

	def full_names(self):
		name=self.first_name+self.second_name
		return name

	def initial_balance(self):
		return  balance
	
	def message(self):

		return "Hello,{} {} Welcome to KCB Mshwari your balance is {}" . format (self.first_name,self.second_name,self.initial_balance)

	def deposit(self):
		deposited_bal= float(input("Enter amount you want to deposit:"))
		self.initial_balance += deposited_bal
		print("\n You deposited:", deposited_bal)

	def withdraw(self):
		withdrawn_bal= float(input("Enter amount withdrawn:"))
		if self.initial_balance >=withdrawn_bal:
			self.initial_balance-=withdrawn_bal
		print("\n You have withdrawn:", withdrawn_bal )
        
        else :
			print("\n sorry Insufficient balance")

	def print_balance(self):
		print("\n  Current Balance=", self.initial_sbalance)
		

		