from itertools import combinations

def solution(sentences, n):
    answer = -1

    keyList = []
    keyCombination = []
    for i,s in enumerate(sentences):
        score = len(s)
        
        data = []
        for spell in s:
            if not spell in keyCombination:                
                keyCombination.extend(spell.lower())                
            if spell.isupper():
                score+=1
            if not spell in data:
                data.append(spell.lower())
        keyList.append((data, score))        
        
    # print(keyList)
    # print(keyList[0])
    result = 0
    a = combinations(keyCombination,n)    
    for item in a:
        sum = 0
        for k in keyList:
            if set(item) == set(k[0]):
                sum += k[1]
        result = max(result,max)

        
    #최대 키를 골라 => 필요한 키도 동일해야하고, 문자열도 동일해아함
    return answer

a = ["line in line", "LINE", "in lion"]
n = 5
solution(a,n)