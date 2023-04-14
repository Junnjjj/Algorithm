import sys
input = sys.stdin.readline

string = list(input().rstrip())

# 대문자와 _ 같이 있으면 에러 출력

isJava = False
isC = False
for w in string:
	if w.isupper():
		isJava = True
	if w == '_':
		isC = True

if isJava and isC:
	print("Error!")
	exit()

if not isJava and not isC:
	print(''.join(string))
	exit()

if string[0] == '_' or string[-1] == '_' or string[0].isupper():
	print("Error!")
	exit()
		
result = []
if isJava:
	for w in string:
		if w.isupper():
			result.append('_')
			result.append(w.lower())
		else:
			result.append(w)

if isC:
	idx = 0
	while idx < len(string):
		if string[idx] == '_':
			idx += 1
			if string[idx] == '_':
				print('Error!')
				exit()
			result.append(string[idx].upper())
		else:
			result.append(string[idx])

		idx += 1


print(''.join(result))