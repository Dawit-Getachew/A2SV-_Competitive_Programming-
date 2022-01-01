def pattern(N):
    if(N==2):
        for i in range(N):
            print(("#"*1+" ")*N)
    if(N==3):
        for i in range(N-1):
            print(("#"*2+" ")*N)
    if(N==4):
        for i in range(N-2):
            print(("#"*3+" ")*N)
pattern(2)
pattern(3)
pattern(4)