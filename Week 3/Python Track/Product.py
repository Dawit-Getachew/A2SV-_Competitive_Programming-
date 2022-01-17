# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = map(int,input().split())
B = map(int,input().split())
cProduct = tuple(product(A,B))
for i in range(len(cProduct)):
    print(cProduct[i],end = " ")