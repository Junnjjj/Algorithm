import sys
input = sys.stdin.readline

def solution(w,k):
	dict = {}

	for i in range(len(w)):
		if w.count(w[i]) >= k:

			if w[i] in dict:
				dict[w[i]] += [i]
			else:
				dict[w[i]] = [i]

	if not dict:
		print(-1)
		return -1

	min_ans = 1e9
	max_ans = 0
	for key,value in dict.items():

		for j in range(len(value) - k + 1):
			size = value[j+k-1] - value[j] + 1

			min_ans = min(min_ans, size)
			max_ans = max(max_ans, size)

	print(min_ans, max_ans)
	return
			 
	
	

t = int(input())
for _ in range(t):
	w = input().rstrip()
	k = int(input())

	solution(w,k)


# 2
# superaquatornado
# 2
# abcdefghijklmnopqrstuvwxyz
# 5

# from collections import defaultdict

# def solution(w,k):  
# 	string,K = w,k
# 	len_str = len(string)    
# 	alpha = defaultdict(list) 
# 	for i in range(len_str): 
# 		if string.count(string[i]) >= K: 
# 			alpha[string[i]].append(i)
			
# 	print(alpha)
# 	if not alpha: 
# 		print(-1)
# 		return 

# 	min_str,max_str = 1e9, 0
# 	for idx_lst in alpha.values():		
# 		for j in range(len(idx_lst) - K + 1):
# 			temp = idx_lst[j+K-1] - idx_lst[j] + 1			

# 			if temp < min_str: 
# 				min_str = temp 
# 			if temp > max_str: 
# 				max_str = temp

# 	print(min_str, max_str)  

# t = int(input())

# for _ in range(t):
# 	W = str(input().rstrip())
# 	K = int(input())
	
# 	solution(W,K)
