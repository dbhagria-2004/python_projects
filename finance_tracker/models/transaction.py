from datetime import date, datetime
from decimal import Decimal

class Transaction:

    def __init__(self, date_str: str, amount_str: str, description: str, user_id: int):

        self.user_id = user_id
        self.date = datetime.strptime(date_str, "%m/%d/%Y").date()
        self.amount = float(amount_str)
        self.description = description

    def getUserId(self):
        return self.user_id
    

    def getAmount(self):
        amount = self.amount
        return amount
    
    def getDate(self) -> str:
        return self.date
    
    def getDescription(self):
        return self.description

    def __str__(self):
        return (f"The transaction: {str(self.id)} was made on {self.date}, it was of {self.amount} dollars and was used for this purpose: {self.description}")