n = int(input())
lst_n = input().split()
m = int(input())
lst_m = input().split()
res_dict = dict()
res_str = ''

for i in lst_n:
    if i in res_dict.keys():
        res_dict[i] += 1
    else:
        res_dict[i] = 1

for i in lst_m:
    if i in res_dict.keys():
        res_str += (str(res_dict[i]) + ' ')
    else:
        res_str += '0 '

print(res_str)
