from collections import deque

INF = 1e9

def solution(alp, cop, problems):
    answer = 0
    
    maxAlp,maxCop = 0,0 # 도달해야하는 최대 알고력, 코딩력
    for i in range(len(problems)):
        maxAlp = max(maxAlp,problems[i][0])
        maxCop = max(maxCop,problems[i][1])
    
    q = deque()
    check = [[INF]*(maxCop+1) for _ in range(maxAlp+1)]
    q.append((alp,cop,0))
    check[alp][cop] = 0

    answer = 1e9
    while q:
        na,nc,cost = q.popleft()        
      
        if na == maxAlp and nc == maxCop:
            answer = min(answer,cost)
            continue
          
        for i,j in (1,0),(0,1): # 1시간씩 공부할 경우
            da,dc = na+i, nc +j
            if da > maxAlp or dc > maxCop:
                continue

            if check[da][dc] > cost+1:
              check[da][dc] = min(check[da][dc],cost+1)
              q.append((da,dc,cost+1))

        for p in problems: # 문제를 풀 경우
            if na < p[0] or nc < p[1]: # 문제를 풀 수 없으면 넘어감
                continue
            da,dc = na+p[2], nc+p[3] # 증가하는 코딩력

            if da > maxAlp or dc > maxCop:
                continue
            
            if check[da][dc] > cost+p[4]:              
              check[da][dc] = cost+p[4]
              q.append((da,dc,cost+p[4]))
        
    return answer

alp = 10
cop = 10
p = [[10,15,2,1,2],[20,20,3,3,4]]

alp = 0
cop = 0
p = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]	
ans = solution(alp,cop,p)
print(ans)