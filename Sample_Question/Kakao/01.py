def checkReverse(string):
    if string[0] == 'R' or string[0] == 'C' or string[0] == 'J' or string[0] == 'A':
        return False
    return True

def solution(survey, choices):
    answer = ''

    choice_dict = {1:3, 2:2, 3:1, 4:0, 5:-1, 6:-2, 7:-3}
    character = [0] * 4 # RT, CF, JM, AN

    size = len(survey)

    for i in range(size):
        s, c = survey[i], choices[i]

        if 'R' in s:
            # RT 인경우
            idx = 0
        elif 'C' in s:
            # CF 인 경우
            idx = 1
        elif 'J' in s:
            # JM 인 경우
            idx = 2
        elif 'A' in s:
            # AN 인 경우
            idx = 3
        
        if checkReverse(s): # 거꾸로되어있으면
            character[idx] -= choice_dict[c]
        else:
            character[idx] += choice_dict[c]

    temp = ['RT', 'CF', 'JM', 'AN']
    for i,j in enumerate(character):
        if j > 0:
            k = 0
            answer += temp[i][k]
        elif j < 0:
            k = 1
            answer += temp[i][k]
        else:
            tmp = sorted(list(temp[i]))
            answer += tmp[0]

    return answer