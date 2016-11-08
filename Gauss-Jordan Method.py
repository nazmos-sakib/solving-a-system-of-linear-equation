a=[]

r1=[2,4,-6,-8]  
r2=[1,3,1,10]
r3=[2,-4,-2,-12]

a.append(r1)
a.append(r2)
a.append(r3)

dpo=0
spo=0

def normalise():
    global dpo
    for i in range(3):
        div = a[i][dpo]
        for j in range(4):
                a[i][j] = a[i][j]/div
    dpo = dpo+1
    return

def subtract():
    global spo
    for i in range(3):
        if i==spo:
            continue
        for j in range(4):
                a[i][j] = a[i][j]-a[spo][j]
    spo = spo+1
    return
            


            
for l in range(3):
    normalise()
    subtract()

print ('x = ',a[0][3]/a[0][0])
print ('y = ',a[1][3]/a[1][1])
print ('z = ',a[2][3]/a[2][2])
