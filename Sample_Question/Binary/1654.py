import sys
input = sys.stdin.readline

n,k = map(int,input().split())
data = [int(input()) for _ in range(n)]

data.sort()
start = 1
end = data[-1]

while start <= end:
    mid = (start + end) // 2
    lines = 0 
    for i in data:
        lines += i // mid
        
    if lines >= k:
        start = mid + 1
    else:
        end = mid - 1
print(end)


# 4 11
# 802
# 743
# 457
# 539