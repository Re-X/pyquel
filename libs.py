import sys, os, traceback, types

def isUserAdmin():

    if os.name == 'nt':
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            print ("Admin check failed, assuming not an admin.")
            return False
        
    elif os.name == 'posix':
        # Check for root on Posix
        return os.getuid() == 0
    
def runAsAdmin(cmdLine=None, wait=False):

    if(isUserAdmin()):
        print("User is admin.")
        return 0

    print("Need elevated privilages.")
    
    import win32api, win32con, win32event, win32process
    from win32com.shell.shell import ShellExecuteEx
    from win32com.shell import shellcon

    script = sys.argv[0] #Script path
        
    cmd = '"%s"' % sys.executable #python-exe path

    params = '"%s"' % script
    cmdDir = ''
    showCmd = win32con.SW_SHOWNORMAL
    lpVerb = 'runas'  # causes UAC elevation prompt.

    win32api.ShellExecute(0, lpVerb, cmd, params, cmdDir, showCmd)

    exit()

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
