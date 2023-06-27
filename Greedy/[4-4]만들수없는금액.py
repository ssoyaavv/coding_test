N = int(input())
N_list = list(map(int,list(input().split())))

N_list.sort()
output_list = []
# 최악의 경우 최솟값 = 리스트에서 가장 큰 값 + 가장 작은값

if N_list[0] > 1 :
    print(1)
else : 
    for i in range(len(N_list)): # 몇 개의 숫자를 더할 것인가
        for j in range(len(N_list)-i+1) : 
            tmp = 0
            for z in range(i) : 
                tmp += N_list[j+z]
            output_list.append(tmp)

    output_list = list(set(output_list))

    for i in range(len(output_list)-1):
        if (output_list[i+1]- output_list[i]) > 1 :
            print(output_list[i]+1)
            break 