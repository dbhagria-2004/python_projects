import sqlite3

class Database():

    def getConnection(self, database:str):
        try:
            connection = sqlite3.connect(database)
            print("Connectin was sucessful")
        except Exception as e:
            print(f" The execption was {e}")
        
        return connection
    

#Used to create Users table to a table
    def addUserTable(self, connection):
        query = """
                CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id  INTEGER,
                name TEXT NOT NULL,
                salary REAL
                )
                """
        try:
            connection.execute(query)
            print("User table was created")
        except Exception as e:
            print(f"Exception was {e}")

# adds a user to users table
    def addUser(self, connection, user):
        user_id = user.getId()
        print(user_id)
        name = user.getName()
        print(name)
        salary = user.getSalary()
        print(salary)

        query ="INSERT INTO users(user_id, name, salary) VALUES (?, ?, ?)" 
        try: 
            connection.execute(query, (user_id, name, salary))
            connection.commit()
            print("The user was added to the table ")

        except Exception as e:
            print(f"This is the exception:{e}")
    
# fetches a user 
    def fetchUser(self, connection, condition: str) -> list[tuple]:
        query = "SELECT * FROM users"
        if condition:
            query += (f" WHERE {condition}")
        try:
            rows = connection.execute(query).fetchall()
            return rows
        except Exception as e:
            print(e)
        

#Used to create Transaction table
    def addTransactionTable(self, connection):
        query = """
                CREATE TABLE IF NOT EXISTS transactions(
                trans_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                amount  REAL,
                date TEXT,
                description TEXT
                )
                """
        try:
            connection.execute(query)
            print("Transaction table was created")
        except Exception as e:
            print(f"Exception was {e}")



# adds transaction to the transaction table
    def addTransaction(self, connection, Transaction):
            user_id = Transaction.getUserId()
            print(user_id)
            amount = Transaction.getAmount()
            print(amount)
            date = Transaction.getDate()
            print(date, type(date))
            description = Transaction.getDescription()
            print(description)

            query ="INSERT INTO transactions(user_id, amount, date, description) VALUES (?, ?, ?, ?)" 
            try: 
                connection.execute(query, (user_id, amount, date, description))
                connection.commit()
                print("The transaction was added to the table ")

            except Exception as e:
                print(f"This is the exception:{e}")
    
# fetches a user 
    def fetchUserTransaction(self, connection, condition: str) -> list[tuple]:
        query = "SELECT * FROM transactions"
        if condition:
            query += (f" WHERE {condition}")
        try:
            rows = connection.execute(query).fetchall()
            return rows
        except Exception as e:
            print(e)
        



    

