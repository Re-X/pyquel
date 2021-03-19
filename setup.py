import mysql.connector
from mysql.connector import errorcode

config = {
  'username': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'port': 3306,
  'raise_on_warnings': True
}

def Connect():
    global config
    global mysql_version
    
    while 1:
        print('\n')
        user = input("Enter username: ")
        password = input("Enter password: ")
        config['password'] = password
        host = input("Enter host : ")        
        try:
            connection = mysql.connector.connect(username = user, password = password, host = host)
            break
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\nERROR: ACCESS DENIED.\n")
            elif err.errno == 2003:
                print("\nERROR: Can't connect to MySQL server on", host)
            else:
                print("\nERROR: Can't connect to MySQL server on", host)
    return connection
























    
