import time, sys
indent=0
Indent_inc=True

try:
    while 1 :
        print(' '*indent,end='')
        print('********')
        time.sleep(0.1)
        
        if Indent_inc:
            indent=indent+1
            if indent==10:
                Indent_inc=False
        else:
            indent=indent-1
            if indent==0:
                Indent_inc=True
            
except KeyboardInterrupt:
    sys.exit()
