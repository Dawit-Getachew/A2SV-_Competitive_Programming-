from collections import Counter
X = int(input())
sSize = Counter(map(int,input().split()))
N = int(input())
sEarning = 0
for j in range(N):
    sizes, x  = map(int,input().split())
    if sizes in sSize and sSize[sizes] >0:
        sSize[sizes] -=1
        sEarning += x
print(sEarning)