
print("\n\n")
print("\t\t\t██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗██╗     ")
print("\t\t\t██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██║     ")
print("\t\t\t██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ██║     ")
print("\t\t\t██╔═══╝   ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ██║     ")
print("\t\t\t██║        ██║   ╚██████╔╝╚██████╔╝███████╗███████╗")
print("\t\t\t╚═╝        ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝\n\n")


import os
from time import perf_counter as now

import mysql.connector

import setup
from libs import *
import cmds

connection = setup.Connect()

print("Connection established.")
os.system("CLS")

cursor = connection.cursor()

print("connected to MySQL server on", setup.config['host'], '\n\n')

cmds.cursor = cursor

pad   = ">>> "
query = ""

while 1:
    query += input(pad)
    
    if not query:
        continue
    
    if (query[-1] != ';'):
        if(query[0] == '@'):
            query = query[1:]
            cmd = cmds.COMMAND(query)
            if(cmd):
                query = cmd
            else:
                query = ""
                continue
                
        elif (query in ("exit, q, quit")):
            break
        elif (query in ('cls', 'clear', 'clearscreen', 'clrscr')):
            os.system('CLS')
            query = ''
            continue
        else:
            query += " "
            pad = " "*8 + "-> "
            continue
    else:
        pad = ">>> "
        
    try:
        cursor.execute(query)
        query = ""
    except mysql.connector.Error as err:
        print("ERROR: {}\n".format(err))
        query = ""
        continue
      
    if(cursor.with_rows):
        T0 = now()
        echo(cursor)
        print("-> executed in {0} secs.\n".format(now()-T0))

os.system("net stop mysql{0}".format(setup.mysql_version))
