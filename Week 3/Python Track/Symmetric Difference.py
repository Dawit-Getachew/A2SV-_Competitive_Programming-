# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
A = set(input().split())
N = int(input())
B = set(input().split())
aDb = A.difference(B)
bDa = B.difference(A)
symmetric = aDb.union(bDa)
symmetric = list(map(int,symmetric))
symmetric.sort()
for i in symmetric: print(i)