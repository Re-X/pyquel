
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

pad   = ">>> "
query = ""

while 1:
    query += input(pad)
    if not query:
        continue
    if (query in ("exit, q, quit")):
        break
    if (query in ('cls', 'clear', 'clearscreen', 'clrscr')):
        os.system('CLS')
        query = ''
        continue
    
    if (query[-1] != ';'):
        query += " "
        pad = " "*8 + "-> "
        continue
    else:
        pad = ">>> "
        
    try:
        cursor.execute(query)
        query = ""
    except mysql.connector.Error as err:
        print("ERROR: {}".format(err))
        query = ""
        continue
      
    if(cursor.with_rows):
        T0 = now()
        echo(cursor)
        print("-> executed in {0} secs.\n".format(now()-T0))

os.system("net stop mysql{0}".format(setup.ver))
