import itertools 
N = int(input())
letter = list(map(str,input().split()))
k = int(input())
counter = 0
letr = list(itertools.combinations(letter,k))
for i in letr:
    if 'a' in i:
        counter += 1
prob = counter / len(letr)
print(round(prob,3))