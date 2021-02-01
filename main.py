import os
import setup

print("\n\n")
print("\t\t\t██████╗ ██╗   ██╗ ██████╗ ██╗   ██╗███████╗██╗     ")
print("\t\t\t██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║██╔════╝██║     ")
print("\t\t\t██████╔╝ ╚████╔╝ ██║   ██║██║   ██║█████╗  ██║     ")
print("\t\t\t██╔═══╝   ╚██╔╝  ██║▄▄ ██║██║   ██║██╔══╝  ██║     ")
print("\t\t\t██║        ██║   ╚██████╔╝╚██████╔╝███████╗███████╗")
print("\t\t\t╚═╝        ╚═╝    ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝\n\n")

config = setup.config
connection = setup.Connect()

print("Connection established.")
os.system("CLS")

cursor = connection.cursor(raw = True)

print("connected to MySQL server on", config['host'], '\n\n')

while 1:
    query = input(">>> ")
    cursor.execute(query)
    if(cursor.with_rows):
        print('\n')
        for i in cursor:
            print(i)
        print("\n")


