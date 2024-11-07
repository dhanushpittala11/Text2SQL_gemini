import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Rahul','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',90)''')
cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',90)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','B',90)''')
cursor.execute('''Insert Into STUDENT values('Akash','Machine Learning','C',90)''')
cursor.execute('''Insert Into STUDENT values('Ujwal','Machine Learning','A',90)''')
cursor.execute('''Insert Into STUDENT values('Diraj','Software Engineering','B',90)''')

## Display all the records
print("The Inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection

connection.commit()
connection.close