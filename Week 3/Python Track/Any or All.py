# Enter your code here. Read input from STDIN. Print output to STDOUT
n, nums= int(input()), input().split()
positive = all([int(num) > 0 for num in nums ])
palindrome = any([num == num[::-1] for num in nums])
print(positive and palindrome)