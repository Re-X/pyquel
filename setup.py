import mysql.connector
from mysql.connector import errorcode

setup_config = (open('setup.config')).read()
exec(setup_config)

def Connect():
    global config
    global mysql_version
    
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
            else:
                print("\nERROR: Can't connect to MySQL server on", config['host'])
    return connection
























    
