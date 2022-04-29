import sys

input = sys.stdin.readline

A = int(input(), 2) 
B = int(input(), 2) 
mask = 2**100000 - 1 
print(bin(A & B)[2:].zfill(6)) 
print(bin(A | B)[2:].zfill(6)) 
print(bin(A ^ B)[2:].zfill(6)) 
print(bin(A ^ mask)[2:].zfill(6)) 
print(bin(B ^ mask)[2:].zfill(6))
