# 엔진의 힘 p, 연료 m, 거리 d
def distance(p,m,d):
    d = d - (p*m*m)/2 
    if d == 0:
        return m
    else:        
        t = (d/(p*m))+m
        return t        

def solution(fuel, powers, distances):
    answer = 0

    # 1~n 까지 우주선
    # fuel 을 모든 우주선에 배분
    # p 에 m 을 넣으면 p 초동안은 p km/s, m 초 후에는 등속도 

    # 우주선들의 도작 시간의 최대 값이 모든 경우의 수 중 최솟값이 되어야 한다.    
    total = 0
    for i in range(len(powers)):
        total += distances[i]
 
    percentage = []
    for i in range(len(powers)):
        temp = distances[i]/powers[i]
        per = ((total)/temp)/100

        percentage.append(int(fuel*per))
      
    for i in range(len(powers)):
        dis = distance(powers[i],percentage[i],distances[i])        
        answer = max(answer, dis)

    answer = int(answer)

    return answer


a = 8
b = [20, 30]
c = [750, 675]

a = 19
b = [40, 30, 20, 10]	
c = [1000, 2000, 3000, 4000]
d = solution(a,b,c)
print(d)
