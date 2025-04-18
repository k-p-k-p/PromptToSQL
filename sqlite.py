import sqlite3

##connect to SQLite
connection=sqlite3.connect("student.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()
## table info 

print(cursor)
table_info= """
Create table student(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT(3));
"""
cursor.execute(table_info)

cursor.execute('''INSERT INTO student VALUES('DEBASHISH','DSA','D',100)''')
cursor.execute('''INSERT INTO student VALUES('NARESH','DATA SCIENCE','A',99)''')
cursor.execute('''INSERT INTO student VALUES('AJITESH','STATISTICS','B',66)''')
cursor.execute('''INSERT INTO student VALUES('SURESH','DSA','A',52)''')
cursor.execute('''INSERT INTO student VALUES('DEBESH','DATA SCIENCE','C',29)''')

print("The inserted records are :")
data=cursor.execute('''select * from student''')

for row in data:
    print(row)

connection.commit()
connection.close()

