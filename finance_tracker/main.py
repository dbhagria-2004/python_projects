from models.transaction import Transaction
from models.user import User
from db.database import Database
import datetime
def main():
    print("Welcome to my app!")
     
    db = Database()
    connection = db.getConnection("data/database.db")
    db.addUserTable(connection)
    db.addTransactionTable(connection)

    trans = Transaction("10/25/2025", "40", "coffee", 101)
    
    db.addTransaction(connection, trans)



    # user1 = User("john", 40000)
    # user2 = User("joe", 33000)
    # print(user1.getId())
    # print(user2.getId())


    # db.addUser(connection, user1)
    # db.addUser(connection, user2)

    list = db.fetchUserTransaction(connection, "user_id = 101")
    print(list)

    # t1 = Transaction("10/25/2004", 33.00, "coffee")
 

    # user1.add_transction(t1)
    # print(f"users income is: {user1.getTotalIncome()}")
    # for i in user1.transactions:
    #     print(i)


if __name__ == "__main__":
    main()  


