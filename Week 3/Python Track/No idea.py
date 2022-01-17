# Enter your code here. Read input from STDIN. Print output to STDOUT
nAndm = input().split()
n = int(nAndm[0])
m = int(nAndm[1])
elements = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0
for i in range(n):
    if elements[i] in A:
        happiness+=1
    if elements[i] in B:
        happiness-=1
print(happiness)