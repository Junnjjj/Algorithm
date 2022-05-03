# 투포인터
# 수들의 합

import sys

input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))


left, right = 0, 1
cnt = 0
while right<=n and left<=right:

    sum_nums = arr[left:right]
    total = sum(sum_nums)

    if total == m:
        cnt += 1

        right += 1

    elif total < m:
        right += 1

    else:
        left += 1

print(cnt)
