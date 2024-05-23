# DP 연습

import sys
input = sys.stdin.readline

# 9252
def solution7():
	a = str(input().rstrip())
	b = str(input().rstrip())
	an = len(a)
	bn = len(b)
	dpStr = [[] for _ in range(bn)]
	dp = [0]*(bn)		


	for i in range(an):
		for j in range(bn-1,-1,-1):

			if a[i] == b[j]:				
				if j == 0:
					dp[j] = 1					
					dpStr[j] = [b[0]]

				else:
					dp[j] = max(dp[:j]) + 1

					idx = dp.index(max(dp[:j]))
					dpStr[j] = dpStr[idx] + [b[j]]



	maxLen = max(dp)
	maxIdx = dp.index(maxLen)	
	if maxLen == 0:
		print(maxLen)
	else:
		print(maxLen)
		print(''.join(dpStr[maxIdx]))


solution7()