# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s1 = input().split()
S2 = sorted(tuple(s1[0]))
out = tuple(permutations(S2,int(s1[1])))
for i in out:
    print("".join(i))
