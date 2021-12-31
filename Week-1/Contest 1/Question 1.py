row = 4
"""  Question 1. A   """
for i in range(1,(2*row)+1,2):
    for j in range(1,(2*row)-i,2):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    print()
"""  Question 1. B   """
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end='')
    print()