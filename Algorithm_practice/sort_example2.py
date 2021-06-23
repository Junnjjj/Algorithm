#python sort library

#Count sort
#assume all value are more then 0 or 0
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0]* (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)): #리스트에 기록된 정렬 정보 확인
  for j in range(count[i]):
    print(i, end= ' ')

print()
#Python sorted library -> 병합 정렬, 최악의 경우 시간 복잡도 O(nlogn) 
array = [7, 5, 9, 0, 3, 1, 6 ,2, 4, 8]    

result = sorted(array)
print(result)

#리스트 변수가 하나 있을 때 내부 원소를 바로 정렬 sort()
array = [7, 5, 9, 0, 3, 1, 6 ,2, 4, 8]    
array.sort()

print(array)

#sort, sorted key 입력으로 받음

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
  return data[1]

result = sorted(array, key = setting)
print(result)