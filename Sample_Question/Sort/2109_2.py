import heapq

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    
data.sort(key=lambda x : x[1])

heap_list = []
for i in range(len(data)):
    heapq.heappush(heap_list, data[i][0])
    
    if len(heap_list) > data[i][1]:
        heapq.heappop(heap_list)
        
print(sum(heap_list))

