def pattern(N):
    if(N==2):
        for i in range(N):
            J=1
            print(("#"*J+" ")*N)
    if(N==3):
        for i in range(N-1):
            J=2
            print(("#"*J+" ")*N)
    if(N==4):
        for i in range(N-2):
            J=3
            print(("#"*J+" ")*N)
pattern(2)
pattern(3)
pattern(4)