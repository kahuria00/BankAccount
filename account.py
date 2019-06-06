from datetime import datetime
class Account:
    def __init__ (self,first_name,second_name):

        self.first_name=first_name
        self.second_name=second_name
        self.balance=0.00
        self.loan=0.00
        self.deposits=[]
        self.withdraws=[]
        self.loans=[]
   
    def message(self):

        return "Hello,{} {} Welcome to KCB Mshwari your balance is {}" . format (self.first_name,self.second_name,self.balance)

    def deposit(self,deposited_bal):
        time=datetime.now()
        object={"time":time,"depositedbal":deposited_bal}
        self.deposits.append(object)
        self.balance= self.balance+deposited_bal
        #self.deposits.append(deposited_bal)
        return "You have deposited{}". format(deposited_bal)
    
    def show_deposits(self):
        for deposited_bal in self.deposits:
            time=deposited_bal["time"]
            formated_time=time.strftime("%c")
            amount=deposited_bal["depositedbal"]
            print("on {} you deposited{}".format(formated_time,amount))

    def withdraw(self,withdrawn_bal):
        #self.withdraws.append(withdrawn_bal)
        time=datetime.now()
        object={"time":time,"withdrawn":withdrawn_bal}
        self.withdraws.append(object)
        if withdrawn_bal<self.balance:
            self.balance=self.balance-withdrawn_bal
            return "you have successfully withdrawn{}" . format(withdrawn_bal)
        else:
            return "sorry you have insufficient balance"
    
    def show_withdraws(self,):
        for withdrawn_bal in self.withdraws:
            time=withdrawn_bal["time"]
            formated_time=time.strftime("%c")
            amount=withdrawn_bal["withdrawn"]
            print("on {} you withdrew {}".format(formated_time,amount))

    
    def show_balance(self,current_bal):
        current_bal=self.balance+self.deposit-self.withdraw
        return "Hello {} {} you current balance is{}" . format(self.first_name,self.second_name,self.current_bal)
    
    def give_loan(self):

       self.total_deposits = []
        for deposited_bal in self.deposits:
            total_deposits.append(deposited_bal['depositedbal'])
            total_deposits = sum(self.deposits)

        if  total_deposits >=5  and  (self.deposited )* 1/3 and self.loan==0: 
        return "you can get a loan"


    