from models.transaction import Transaction

class User():
    user_id = 10
    def __init__(self, name: str, salary: float):
        User.user_id += 1
        self.name = name 
        self.user_id = User.user_id
        self.transactions = []
        self.salary = salary

    def getId(self):
        return self.user_id
    
    def getName(self):
        return self.name

    def addTransction(self, tran: Transaction):
        self.transactions.append(tran)
    
    def getTrans(self):
        return self.transactions
    

    def getSalary(self):
        income = self.salary
        return income
    
    def getTotalExpense(self):
        amount = []
        user_trans = self.getTrans()
        for i in user_trans:
            amount.append(i.getAmount())
        return sum(amount)
    





        
        
