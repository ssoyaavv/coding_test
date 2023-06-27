S = list(input())

tmp = S[0]
cnt = 0

# 숫자가 바뀌는 순간이 몇 번 있었는지 확인
for i in range(1,len(S)) : 
    if tmp != S[i] :
        cnt += 1
    tmp = S[i]

if cnt == 0 or cnt == 1 :
    print(cnt)
else : 
    if cnt%2 == 0 : 
        print(int(cnt/2))
    else :
        print(int(cnt/2)+1)