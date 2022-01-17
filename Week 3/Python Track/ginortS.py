# Enter your code here. Read input from STDIN. Print output to STDOUT
s=input()
lower,upper,odd,even=[],[],[],[]

for i in s:
    if i.islower():
        lower.append(i)
        lower.sort()
    elif i.isupper():
        upper.append(i)
        upper.sort()
    elif i.isdigit():
        if int(i)%2==0:
            even.append(i)
            even.sort()
        elif int(i)%2!=0:
            odd.append(i)
            odd.sort()
print(''.join(lower),''.join(upper),''.join(odd),''.join(even),sep='')