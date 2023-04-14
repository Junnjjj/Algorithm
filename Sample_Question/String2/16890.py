# import sys
# input = sys.stdin.readline

# a = list(input().rstrip())
# b = list(input().rstrip())

# a.sort()
# b.sort(reverse=True)

# size = len(a)
# result = ['?'] * size
# left = 0
# right = size-1

# a_idx,b_idx = 0,0

# for i in range(size):
# 	if i % 2 == 0:
# 		# 구사과 턴		
# 		if a[i] < b[i]:
# 			result[left] = a[a_idx]
# 			a_idx += 1
# 			left += 1
# 		else:
# 			result[right] = b[b_idx]
# 			b_idx += 1
# 			right -= 1
# 	else:
# 		if b[i] > a[i]:
# 			result[left] = b[b_idx]
# 			b_idx += 1
# 			left += 1
# 		else:
# 			result[right] = a[a_idx]
# 			a_idx += 1
# 			right -= 1

# 	print(result)
			
# print(result)