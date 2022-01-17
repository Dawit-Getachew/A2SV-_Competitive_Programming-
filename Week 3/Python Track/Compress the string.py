# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s  = input()    
for key, value in groupby(s):
    group_obj = len(list(value)), int(key)
    print(tuple(group_obj), end = " ")