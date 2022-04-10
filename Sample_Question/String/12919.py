import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def check(now):
    if now == S:
        return 1
    if len(now)<=len(S):
        return 0

    answer = 0
    if now[-1] == 'A':
        answer = check(now[:-1])
    
    if answer == 1:
        return 1

    if now[0] == 'B':
        temp = now[::-1]
        answer = check(temp[:-1])

    return answer

answer = check(T)
print(answer)