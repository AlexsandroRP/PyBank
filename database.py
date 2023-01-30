import sqlite3 as lite


# Creating connection
con = lite.connect('users.db')

# Creating tables
Q1 = (''' CREATE TABLE Users
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nameAccount TEXT,
    password TEXT,
    balance REAL NOT NULL,
    account INTEGER NOT NULL);''')

Q2 = ('''CREATE TABLE Transactions
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    trans TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    date TEXT,
    time TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(id)
    );''')    

# con.execute(Q1)
# con.execute(Q2)
