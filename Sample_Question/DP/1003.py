import sys

input = sys.stdin.readline

t = int(input())
zero = [1,0,1]
one = [0,1,1]

def fibo(n):
    if 3 <= n :
        for i in range(3, n+1) :
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    
    return zero[n], one[n]

ans = []
for i in range(t) : #[3]
    a = int(input()) #[0,1,3]
    z,o = fibo(a)
    ans.append((z,o))

for item in ans:
  print(item[0], item[1])