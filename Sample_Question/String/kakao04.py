from collections import deque
moves = [(1,0), (-1,0), (0,1), (0,-1)]

def findIllegal(p):
    people = []
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P': # 사람일 경우
              people.append([i,j])

    if len(people) == 0:
      return 1
    

    for person in people:
      
      q = deque()
      person += [0] # 거리
      q.append(person)
      visited = [[False] * 5 for _ in range(5)] # 사람 마다 시도  
    
      while q:              
          dr,dc,length = q.popleft()          
          visited[dr][dc] = True

          nr,nc = dr,dc          

          for move in moves:
              nr = dr + move[0]
              nc = dc + move[1]              
                          
              # 범위 벗어나거나 파티션을 만날 때
              if nr < 0 or nc < 0 or nr >= 5 or nc >= 5 or p[nr][nc] == 'X':
                  continue

              if not visited[nr][nc] and p[nr][nc] != 'P': # 방문하지 않았다면 방문처리
                  visited[nr][nc] = True
                  q.append([nr,nc,length+1])                  
              elif p[nr][nc] == 'P' and not visited[nr][nc]: # 다른 사람 만나면                  
                  if length+1 <= 2: # 맨하튼 거리가 2 이하면    
                    return 0
                     
    return 1

# place = ["POOOP", 
#          "OXXOX", 
#          "OPXPX", 
#          "OOXOX", 
#          "POXXP"]

# print(findIllegal(place))

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

for place in places:  
  print(findIllegal(place))