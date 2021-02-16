import mysql.connector

def CREATE_TABLE():
    global table
    print()
    query = "CREATE TABLE "
    if(not table):
        query += input("Table name: ")
        
    query += "( "
    n = int(input("Degree: "))
    
    for i in range(1, n+1):
        print()
        field = input("Field {0}: ".format(i))
        if(not field):
            query += ""
            break
        
        if(i > 1):
            query += ", "
            
        query += "{0} ".format(field)
        query += input("Datatype: ").upper() + " "
        query += input("Properties: ").upper()

    print()
    foreign_key = input("Foreign Key: ")
    if(foreign_key not in ('', "NULL")):
        ref = input("\tReference: ")
        query += ", FOREIGN KEY ({0}) REFERENCES {1}({0})".format(foreign_key, ref)

    query += ");"
    print("->", query)
    print()
    return query

def ADD_RECORDS(args = ['0']):
    global table

    try:
        n = int(args[0])
    except:
        n = 1
    
    if(not table):
        table = input("Table name: ")
    execute("DESC {0}".format(table))
    columns = cursor.fetchall()
    query = "INSERT INTO {0} VALUES ".format(table)

    k = 1
    
    while k*(n>0) <= n:
        print("\nRecord {0}:".format(k))
            
        values = "("
        for i in range(len(columns)):
            value = input("{0}: ".format(columns[i][0]))
            if(not value):
                value = ""
                k = 0
                break
            elif(value.lower() == 'null'):
                values += "NULL"
            else:
                values += "\"{0}\"".format(value)
            if(i == len(columns) - 1):
                       values += ")"
            else:
                       values += ", "

        if(k == 0):
            break
        if(k > 1):
            query += ", "
        query += values
        k+=1
        
    query += ';'
    print("->", query)
    print()
    return query

def DELETE(condition):
    condition = "{0} = \'{1}\'".format(condition[0], condition[1])
    query = "DELETE FROM {0} WHERE {1};".format(table, condition)
    print('->', query)
    print()
    return query

def ECHO(args = ['*']):
    clauses = ('WHERE', 'HAVING', 'GROUP BY', 'ORDER BY')
    args = ' '.join(args)
    args = args.split(',')
    args = ' '.join(args)

    for clause in clauses:
        if(args.find(clause) != -1):
            args = args.split(clause)
            break
    
    fields = (args[0].strip()).split()
    fields = ', '.join(fields)
    if(not fields.strip()):
        fields = '*'
    try:
        conditions = (args[1].strip()).split()
        conditions = ' '.join(conditions)
    except:
        conditions = ""
        
    if(conditions):
        query = "SELECT {1} FROM {0} {2} {3};".format(table, fields, clause, conditions)
    else:
        query = "SELECT {1} FROM {0};".format(table, fields)
        
    return query


commands = {
               "CREATE TABLE": CREATE_TABLE,
               "ADD": ADD_RECORDS,
               "DELETE": DELETE,
               "SELECT": ECHO,
               "ECHO": ECHO
           }

cursor = None
table = None

def execute(query):
    try:
        cursor.execute(query)
    except mysql.connector.Error as err:
        print("ERROR: {}\n".format(err))
    
def COMMAND(cmd):
    global table

    cmd = cmd.upper()
    if(cmd not in commands.keys()):
        cmd = cmd.split( )
        try:
            table = cmd[0]
            try:
                args = cmd[2:]
            except:
                args = 0
            cmd = (cmd[1]).lower()
            if(args):
                query = commands[cmd](args)
            else:
                query = commands[cmd]()
            table = None
            return query
        except:
            table = None
            print("Unidentified external command")
            return 0
    else:
        query = commands[cmd]()
        return query

