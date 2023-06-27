r, l = input().split(' ') # row, low

min_list = []
for i in range(int(r)):
    l_list = list(map(int,input().split(' ')))
    l_list.sort()

    min_list.append(l_list[0])

min_list.sort(reverse=True)
print(min_list[0])