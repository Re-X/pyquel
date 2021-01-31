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
    print("\n\t\t\t\t██╗      ██████╗  ██████╗ ██╗███╗   ██╗")
    print  ("\t\t\t\t██║     ██╔═══██╗██╔════╝ ██║████╗  ██║")
    print  ("\t\t\t\t██║     ██║   ██║██║  ███╗██║██╔██╗ ██║")
    print  ("\t\t\t\t██║     ██║   ██║██║   ██║██║██║╚██╗██║")
    print  ("\t\t\t\t███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║")
    print  ("\t\t\t\t╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝\n\n\n")
    while 1:
        config['username'] = input("Enter username: ")
        config['password'] = input("Enter password: ")
        hosttemp           = input("Enter host (default - localhost): ")
        if(hosttemp != ''):
            config['host'] = hosttemp
        try:
            connection = mysql.connector.connect(**config)
            break
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\nERROR: ACCESS DENIED.\n")
            elif err.errno == 2003:
                print("\nERROR: Can't connect to MySQL server on", config['host'])
    return connection
    
