import sys
t = int(sys.stdin.readline()) # 테스트 케이스의 개수

for _ in range(t):
    n = int(sys.stdin.readline()) # 전화번호의 수
    phone = [sys.stdin.readline().strip() for _ in range(n)] # n개 만큼 입력(문자열로)
    phone.sort() # 정렬

    for i in range(n-1):
        length = len(phone[i])
        if phone[i] == phone[i+1][:length]: # 접두사끼리만 비교
            print('NO')
            break
    else:
      print('YES')

