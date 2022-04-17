from datetime import datetime,timedelta


#1 차 시도
# def solution(lines):
#     answer = 0
    
    
#     # 1초간 처리하는 요청의 최대 개수    
#     firstTimeList = lines[0].split(' ')
#     tempTime = datetime.strptime(firstTimeList[0]+" "+firstTimeList[1], '%Y-%m-%d %H:%M:%S.%f')
    
#     dates = []
    
    
#     while True:
#         afterOneSecond = tempTime + timedelta(seconds=1)    
#         print(tempTime)
        
#         count = 0
#         for line in lines:            
#             line_list = line.split(' ')
#             # line_list[0] : 년,월,일 / line_list[1] : 시,분,초,밀리초 / line_list[2] : 처리시간
#             date_time_obj = datetime.strptime(line_list[0]+" "+line_list[1], '%Y-%m-%d %H:%M:%S.%f')
            
#             process_time = line_list[2][:-1]            
#             process_time = timedelta(seconds=float(process_time))
                                    
#             endPoint = date_time_obj + process_time
#             if not endPoint in dates:
#                 dates.append(endPoint)
            
#             # 범위 안에 있으면     
#             if date_time_obj < tempTime:
#                 if endPoint >= tempTime:
#                     count += 1
#             elif tempTime <= date_time_obj < afterOneSecond:
#                 count += 1            
        
#         answer = max(answer, count)
        
#         if afterOneSecond > max(dates):
#             print('maxDates : ',max(dates))
#             break
#         tempTime = afterOneSecond
    
#     return answer


def solution(lines):
    answer = 0
    
    start_time = []
    end_time = []
    for line in lines:
        line_list = line.split(' ')
        end_time_obj = datetime.strptime(line_list[0]+" "+line_list[1], '%Y-%m-%d %H:%M:%S.%f')
        end_time.append(end_time_obj)
        
        process_time = line_list[2][:-1]            
        process_time = timedelta(seconds=(float(process_time)))
        
        
        start_time_obj = end_time_obj - process_time + timedelta(seconds=0.001)    
        start_time.append(start_time_obj)
        
        
  # 문제 닷기 잘 읽기
  # 여기 잘 모르겠음 .. 
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):            
            if cur_end_time > start_time[j] - timedelta(seconds=1):                
                cnt += 1
        if cnt == 7:
          print(cur_end_time)
        answer = max(answer, cnt)
    
    return answer

  
a = 	["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
b= solution(a)
print(b)