# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

A = int(input())
B = int(input())
M = math.atan2(A,B)
M = round(math.degrees(M))
print(M,chr(176),sep="")