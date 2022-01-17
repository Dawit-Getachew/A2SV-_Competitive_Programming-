if __name__ == '__main__':
    N = int(input())
    lis=[]
    for i in range(N):
        n = input().split()
        if n[0]=="insert":
            lis.insert(int(n[1]),int(n[2]))
        elif n[0]=="append":
            lis.append(int(n[1]))
        elif n[0]=="pop":
            lis.pop()
        elif n[0]=="print":
            print(lis)
        elif n[0]=="sort":
            lis.sort()
        elif n[0]=="reverse":
            lis.reverse()
        elif n[0]=="remove":
            lis.remove(int(n[1]))
        i=i+1
