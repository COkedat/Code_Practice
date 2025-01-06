str = input()
str_list = str.split(' ')
answer = 0
for i in str_list:
    if bool(i):
        answer+=1

print(answer)