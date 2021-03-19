import mysql.connector

def CREATE_TABLE():
    print()
    query = "CREATE TABLE "
    query += input("Table name: ")
        
    query += "( "
    try:
        n = int(input("Degree: "))
    except Exception as e:
        print(e)
        return 0
    
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
    return query

def ADD_RECORDS(args = ['0']):
    global table
    if(str(args[0]).upper() == 'CSV'):
        return ADD_CSV(args[1])
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

    print()
    query += ';'
    return query

def ADD_CSV(filepath):
    with open(filepath) as f:
        values = f.read().split('\n')
        for i in range(len(values)):
            values[i] = '('+values[i]+')'
    query = "INSERT INTO {0} VALUES {1};".format(table, ', '.join(values))
    return query

def DELETE(conditions):
    conditions = ' '.join(conditions)
    query = "DELETE FROM {0} WHERE {1};".format(table, conditions)
    return query

def UPDATE(args):
    args = ' '.join(args)
    args = args.split('set')
    condition = args[0].strip()
    value = args[1].strip()
    query = "UPDATE {0} SET {1} WHERE {2};".format(table, value, condition)
    return query

def DROP():
    query = "DROP TABLE {0}".format(table)
    return query

def TRUNCATE():
    query = "TRUNCATE TABLE {0};".format(table)
    return query

def ECHO(args = ['*']):
    clauses = ('WHERE', 'HAVING', 'GROUP BY', 'ORDER BY')
    args = ' '.join(args)
    args = args.upper()
    for clause in clauses:
        if(args.find(clause) != -1):
            args = args.split(clause)
            break
    else:
        args = (args,)
    fields = (args[0].strip()).split(' ')
    fields = ' '.join(fields)
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
    #print('->', query)
    return query


commands = {
               "CREATE TABLE": CREATE_TABLE,
               "ADD": ADD_RECORDS,
               "DELETE": DELETE,
               "SELECT": ECHO,
               "ECHO": ECHO,
               "UPDATE": UPDATE,
               "TRUNCATE": TRUNCATE,
               "DROP": DROP
           }
cmds = commands.keys()
cursor = None
table = None

def execute(query):
    try:
        cursor.execute(query)
        return 1
    except mysql.connector.Error as err:
        print("ERROR: {}\n".format(err))
        return 0
    
def COMMAND(cmd):
    global table

    if(cmd.upper() not in cmds):
        cmd = cmd.split()
        table = cmd[0]
        if(len(cmd)==1):
            return SetContext(table)
        args = cmd[2:]

        cmd = (cmd[1]).upper()
        
        if(cmd not in cmds):
            print('ERROR: Unknown external command.\n')
            return 0
            
        try:
            if(args):
                query = commands[cmd](args)
            else:
                query = commands[cmd]()
        except Exception as e:
            print('Error:', e)
            query = 0
        return query
    
    else:
        query = commands[cmd.upper()]()
        return query


def SetContext(table):
    db = None
    if('.' in table):
        table = table.split('.')
        db = table[0]
        table = (table[1]).lower()
    
    if(not db):
        v = execute('show tables')
        if(not v):
            return 0
        db = cursor.column_names[0].split('_')[-1]
        
    else:
        execute('show tables in {0}'.format(db))
    tables = cursor.fetchall()
    if (table.lower(),) in tables:
        print('context {0} set.\n'.format(table))
        return ('context', db+'.'+table)
    else:
        print('no table {0} exists in {1}.\n'.format(table, db))
        return 0


def echo(cursor):
    try:
        data = cursor.fetchall()
    except Exception as e:
        print("ERROR:", e, end = '\n\n')
        return 0

    columns = cursor.column_names

    widths = list(map(len, (col for col in columns)))

    for i in data:
        for j in range(len(i)):
            if widths[j] < len(str(i[j])):
                widths[j] = len(str(i[j]))
                
    tavnit = ' |'
    separator = ' +' 

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print('\n')
    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in data:
        print(tavnit % row)
    print(separator)
    print('\n')
