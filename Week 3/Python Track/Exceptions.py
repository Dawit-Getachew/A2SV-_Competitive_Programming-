# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except BaseException as err:
        print("Error Code:", err)