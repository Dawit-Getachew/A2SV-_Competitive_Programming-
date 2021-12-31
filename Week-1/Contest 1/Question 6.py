m=[]
for i in range(int(input())):
    k = input()
    m.append(k)
print(m)
for j in range(0,len(m)-1):
    for i in range(0,len(m)-1):
        if(int(m[i])==0):
            temp=m[i+1]
            m[i+1]=m[i]
            m[i]=temp
print(m)