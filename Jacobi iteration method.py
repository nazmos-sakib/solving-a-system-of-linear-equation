
x1=0
x2=0
x3=0

def x1_func():
    global x2
    global x3
    x1 = (5-x2-x3)/2
    return x1

def x2_func():
    global x1
    global x3
    x2 = (15-3*x1-2*x3)/5
    return x2

def x3_func():
    global x2
    global x1
    x3 = (8-2*x1-x2)/4
    return x3

for i in range(5):
    tx1 = x1_func()
    tx2 = x2_func()
    tx3 = x3_func()
    
    x1 = tx1
    x2 = tx2
    x3 = tx3

    print (i+1,' iteration valus are\n',x1,'\n',x2,'\n',x3,'\n')
    
