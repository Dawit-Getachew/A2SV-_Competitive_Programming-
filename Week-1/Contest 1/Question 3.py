def patternOne(N):
    if(N==2):
        for i in range(N):
            J=1
            print(("#"*J+" ")*N)
def patternTwo(N):
    if(N==3):
        for i in range(N-1):
            J=2
            print(("#"*J+" ")*N)
def patternThree(N):
    if(N==4):
        for i in range(N-2):
            J=3
            print(("#"*J+" ")*N)
patternOne(2)
patternTwo(3)
patternThree(4)