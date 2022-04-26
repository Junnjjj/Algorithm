from bisect import bisect_left
from collections import defaultdict
from itertools import combinations


# 모든 경우의수를 만들어 해당 경우의 수를 키값으로 하는 딕셔너리에 score를 저장한다.
def solution(info, query):
    answer = []
    dic = {}
    comb = [0, 1, 2, 3]
    for i in info:
        person = i.split()
        conditions = person[:-1]
        score = int(person[-1])
        for j in range(5):
            for k in list(combinations(comb, j)):
                temp = conditions.copy()
                for idx in k:
                    temp[idx] = '-'
                key = ''.join(temp)
                if key in dic:
                    dic[key].append(score)
                else:
                    dic[key] = [score]
                  
    for value in dic.values():  # 딕셔너리 내 모든 값 정렬
        value.sort()

    print(dic)
  
    for i in query:
        q_list = []
        for j in i.split():
            if j == 'and':
                continue
            q_list.append(j)

        target = int(q_list[-1])
        key = ''.join(q_list[:-1])

        if key in dic:
            hubo_list = dic[key]

            index = bisect_left(hubo_list, target)
            answer.append(len(hubo_list) - index)
        else:
            answer.append(0)
            continue

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

ans = solution(info, query)
print(ans)