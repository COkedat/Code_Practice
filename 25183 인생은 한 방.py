N = int(input())
word = list(input())
for i in range(N):
    word[i]=int(ord(word[i]))
cnt=1
isOK=False
for i in range(0,N-1):
    if(word[i] == word[i+1] + 1 or word[i] == word[i+1] - 1):
        cnt+=1
        if(cnt>=5):
            isOK=True
    else:
        cnt=1
    
if(isOK):
    print("YES")
else:
    print("NO")