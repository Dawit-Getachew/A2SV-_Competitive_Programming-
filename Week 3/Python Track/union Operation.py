# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eRollNum = set(input().split())
b = int(input())
fRollNum = set(input().split())
total=list(eRollNum.union(fRollNum))
print(len(total))
