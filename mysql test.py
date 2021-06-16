import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root", password="9944394985", database="office")
'''
This database parameter is used to denote which database that we are 
going to work
'''
my_cursor = dataBase.cursor() # This method is pointed to database where we can fetch the data

my_cursor.execute("create database office") # To create database

my_cursor = dataBase.cursor() # This method is pointed to database where we can fetch the data

my_cursor.execute("select * from information") # will Get the data from database

my_cursor.execute("show tables")   # This will create a new database

col = "insert into information (Employee_name, Employee_address, Age) values (%s,%s,%s)"
record = ("Sharook", "pondycherry", "23")

my_cursor.execute("create table information (Employee_name varchar(100), Employee_address varchar(100), Age int)")

my_cursor.execute(col,record)

dataBase.commit()    # This method is required to make changes in tables

for i in my_cursor:
    print(i)



