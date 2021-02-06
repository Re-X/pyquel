
def echo(cursor):
    print('\n')
    
    data = cursor.fetchall()
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

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in data:
        print(tavnit % row)
    print(separator)
    print('\n')
