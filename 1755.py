number_dict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',0:'zero'}
str_dict = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
inp = input().split(' ')

start = int(inp[0])
end = int(inp[1])

num_list = range(start, end+1)
str_list = []

for i in num_list:
    if len(str(i))==1:
        str_list.append(number_dict[i])
    else:
        str_list.append(number_dict[i//10] + " " + number_dict[i%10])

str_list.sort()

cnt = 0
for j in str_list:
    tmp = j.split(' ')
    if len(tmp)==1:
        print(str_dict[tmp[0]], end = '')
    else:
        print(str_dict[tmp[0]], end = '')
        print(str_dict[tmp[1]], end = '')
    cnt+=1
    if (cnt%10==0):
        print()
        continue
    print('',end=' ')