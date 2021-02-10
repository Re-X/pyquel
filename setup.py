import mysql.connector
from mysql.connector import errorcode
from libs import *

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
                if(config['host'] in ('127.0.0.1', 'localhost')):
                    b = input("Start mysql service? ")
                    if(b in ('Y', "Yes", "True", 'y', 'yes')):
                        runAsAdmin()
                        
                        try:
                            ver = eval(input("mysql version: "))
                            if(type(ver)==float):
                                mysql_version = int(ver*10)
                                
                        except:
                            print('->', mysql_version, sep = '')
                        
                        os.system("net start mysql{0}".format(mysql_version))
                        connection = mysql.connector.connect(**config)
                        break
            else:
                print("\nERROR: Can't connect to MySQL server on", config['host'])
    return connection
























    
