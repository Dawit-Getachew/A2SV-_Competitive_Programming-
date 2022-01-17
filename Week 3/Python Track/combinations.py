# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s = input().split()
sortedS = sorted(tuple(s[0]))
for i in range(1,int(s[1])+1):
    f = tuple(combinations(sortedS,i))
    for char in f:
        print("".join(char))
