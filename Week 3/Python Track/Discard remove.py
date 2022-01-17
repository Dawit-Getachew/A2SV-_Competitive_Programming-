n = int(input())
s = set(map(int, input().split()))
numCommand = int(input())
for i in range(numCommand):
    paramList = input().split()
    if paramList[0] == "pop":
        s.pop()
    elif paramList[0] == "remove":
        s.remove(int(paramList[1]))
    elif paramList[0] == "discard":
        s.discard(int(paramList[1]))
print(sum(s))