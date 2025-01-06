#3의 배수
num = input()
cnt = 0

def getX(num):
    val=0
    list(num)
    for i in num:
        val+=int(i)
    return str(val)

while(int(num)>=10):
    num = getX(num)
    cnt+=1

print(str(cnt))
if (int(num)%3==0):
    print("YES")
else:
    print("NO")