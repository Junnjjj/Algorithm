import sys
input = sys.stdin.readline

def solution(string):
	vowel = ['a','e','i','o','u']

	check = 0
	for v in vowel:
		if v not in string:
			check += 1

	if check == 5:
		return False

	for i in range(1,len(string)):
		if string[i] == string[i-1]:

			if string[i] == 'e' or string[i] == 'o':
				continue
			else:
				return False
	
	check = 1 if string[0] in vowel else 0
	check2 = 1 if string[0] not in vowel else 0
		
	for i in range(1,len(string)):
		if string[i] in vowel:
			check += 1			
			check2 = 0
		else:
			check2 += 1
			check = 0

		if check == 3 or check2 == 3:
			return False
						
	return True

while True:
	str = input().rstrip()
	if str == 'end':
		break
	result = solution(str)
	if result:
		print('<'+str+'>','is acceptable.')
	else:
		print('<'+str+'>','is not acceptable.')
		