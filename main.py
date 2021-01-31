import os
import setup

config = setup.config
connection = setup.Connect()

print("Connection established.")
os.system("CLS")

cursor = connection.cursor(raw = True)

print("connected to MySQL server on", config['host'], '\n\n')

input(">>> ")

