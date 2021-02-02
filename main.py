
print("\n\n")
print("\t\t\t██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗██╗     ")
print("\t\t\t██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██║     ")
print("\t\t\t██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ██║     ")
print("\t\t\t██╔═══╝   ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ██║     ")
print("\t\t\t██║        ██║   ╚██████╔╝╚██████╔╝███████╗███████╗")
print("\t\t\t╚═╝        ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝\n\n")


import os
import setup
from libs import *
from mysql.connector import FieldType
import mysql.connector


connection = setup.Connect()

print("Connection established.")
os.system("CLS")

cursor = connection.cursor(raw = True)

print("connected to MySQL server on", setup.config['host'], '\n\n')

def echo(data):
    print('\n')
    for i in data:
        for j in i:
            print(j.decode("utf-8"), end = '')
        print()
    print("\n")

while 1:
    query = input(">>> ")
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("ERROR: {}".format(err))
        continue
      
    if(cursor.with_rows):
        data = cursor.fetchall()
        echo(data)

