import sys
input = sys.stdin.readline


string = input().rstrip()
string = list(string)


idx = 0
while idx < len(string):

	word = False
	alpha_size = 0
	if string[idx] == 'w':
		alpha_size += 1

		while True:
			idx += 1
			if idx > len(string):
				print(0)
				exit()
			
			if string[idx] != 'w':
				break
			alpha_size += 1
			
		temp = ['o']*alpha_size + ['l']*alpha_size + ['f']*alpha_size
		if (idx+(3*alpha_size)) > len(string):
			print(0)
			exit()
		
		if string[idx:idx+(3*alpha_size)] != temp:
			print(0)
			exit()
		else:
			idx += alpha_size*3

	else:
		print(0)
		exit()

print(1)
			