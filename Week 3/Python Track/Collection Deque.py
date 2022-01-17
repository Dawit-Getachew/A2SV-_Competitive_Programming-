# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    choice = input().split()
    if choice[0] == "append":
        d.append(choice[1])
    elif choice[0] == "appendleft":
        d.appendleft(choice[1])
    elif choice[0] == "pop":
        d.pop()
    elif choice[0] == "popleft":
        d.popleft()
print(*d)