
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
from time import perf_counter as now
from libs import *


connection = setup.Connect()

print("Connection established.")
os.system("CLS")

cursor = connection.cursor()

print("connected to MySQL server on", setup.config['host'], '\n\n')

main_cursor = cursor

while 1:
    query = input(">>> ")
    
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("ERROR: {}".format(err))
        continue
      
    if(cursor.with_rows):
        T0 = now()
        echo(cursor)
        print("-> executed in {0} secs.\n".format(now()-T0))
        
