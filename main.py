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

input(">>> ")

