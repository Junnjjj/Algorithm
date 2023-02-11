from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
	u, v = map(int, input().split())

	graph[u].append(v)
	graph[v].append(u)


def bfs():
	q = deque()

	count = 0
	for i in range(1, n + 1):

		if visited[i]:
			continue

		q.append(i)
		count += 1
		visited[i] = True
		while q:
			popNode = q.popleft()

			for next in graph[popNode]:
				if not visited[next]:
					q.append(next)
					visited[next] = True

	return count


print(bfs())
