
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
context = ''
while 1:
    query += input(pad)

    if(context and query[0] != '@'):
        query = '@'+context+' '+query.strip()
    else:
        query = query.strip()

    if not query:
        continue
    
    if (query[-1] != ';'):
        if(query[0] == '!'):
            if(query == '!admin'):
                runAsAdmin()
                query = ''
                continue
            else:
                os.system(query[1:])
                print()
                query = ''
                continue
        elif(query[0] == '@'):
            if(query[-1] in ('.', '\\', '@')):
                context = ''
                pad = '>>>'
                query = ''
                continue
            query = query[1:]
            cmd = cmds.COMMAND(query)
            if(cmd):
                query = cmd
                if(cmd[0] == 'context'):
                    query = ''
                    context = cmd[1]
                    pad = '@{0}: '.format(context)
                    continue
            else:
                query = ''
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
        if(context):
            context = ''
            query = ''
            pad = '>>> '
            continue
        pad = '>>> '
        
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

