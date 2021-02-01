import mysql.connector
from mysql.connector import errorcode

config = {
  'username': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'raise_on_warnings': True
}

def Connect():
    global config
    
    while 1:
        print('\n')
        user = input("Enter username: ")
        if(user != ''):
            config['username'] = user
        else:
            print('->', config['username'], sep = '')
        password = input("Enter password: ")
        if(password != ''):
            config['password'] = password
        else:
            print('->', config['password'], sep = '')
        host = input("Enter host : ")
        if(host != ''):
            config['host'] = host
        else:
            print('->', config['host'], sep = '')
        
        try:
            connection = mysql.connector.connect(**config)
            break
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\nERROR: ACCESS DENIED.\n")
            elif err.errno == 2003:
                print("\nERROR: Can't connect to MySQL server on", config['host'])
    return connection
























    
