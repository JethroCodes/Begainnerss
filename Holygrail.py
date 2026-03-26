import sqlite3

conn = sqlite3.connect('Holygrail.db')

query = (''' CREATE TABLE BMR_INFO
        AGE INTEGER NOT NULL,
        NAME TEXT NOT NULL,
        BMR FLOAT NOT NULL,
        

''')
