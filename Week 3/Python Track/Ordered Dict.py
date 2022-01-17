# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n, item_list = int(input()), OrderedDict()
for _ in range(n):
    item, price = input().rsplit(' ',1)    
    item_list.setdefault(item, 0)
    item_list[item] += int(price)
[print(i, v) for i, v in item_list.items()]