INF = 1e9

def solution(n, paths, gates, summits):
    answer = []

    # 노드의 개수 n, 등산로 정보 paths, 출입구 번호 gates, 산봉우리 번호 summits

    # intensity 가 최소가 되는 등산 코스에 포함된 산봉 우리 번호

    # intensity 최솟값
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i,j,k in paths:
        graph[i][j] = k
        graph[j][i] = k

    for k in range(1,n+1):
      for a in range(1,n+1):
        for b in range(1,n+1):
          graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for i in range(1,n+1):
        for j in range(1,n+1):
            print(graph[i][j], end=' ')
        print()


    return answer

n = 7
p = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
g = [1]
s = [2,3,4]

solution(n,p,g,s)