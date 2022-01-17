# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
total = set()
for i in range(n):
    total.add(input())
print(len(total))