import heapq

def solution(food_times, k):
    if sum(food_times) <= k : 
        return (-1)
    
    # tuple로 만들기 
    food_times = [(food, idx+1) for idx, food in enumerate(food_times)] # idx, food 순서 중요

    # list to heap
    heapq.heapify(food_times)
    cnt = 0
    before_num = 0
    
    # print(food_times)
    
    while True : 
        num = food_times[0][0] # min_num
        length = len(food_times)
        
        if (k - cnt) >= length * (num-before_num) : 
            cnt += length * (num-before_num)
            # 중복값 몇 개 있는지 세는 것 보다, 바로 while문 조건을 넣는게 더 가벼움
            min_num = heapq.heappop(food_times)
            while min_num == food_times[0][0] :
                heapq.heappop(food_times)
                     
            before_num = min_num[0]
        else : 
            idx = (k-cnt)%len(food_times)
            
            # 정렬 idx만 가져와서 배열 만들기
            idx_list = [index for food, index in food_times]
            # heap으로 만들어서 pop
            heapq.heapify(idx_list)
            # print(idx_list)
            if idx == 0 :
                return idx_list[0]
            else : 
                final_idx = 1
                for i in range(idx+1) : 
                    final_idx = heapq.heappop(idx_list)
                return final_idx

    return -1
