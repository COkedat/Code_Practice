"""입력
n과 xi가 주어짇나. n은 10만 이하ㅇ고, xi는 젗ㄹ댓값이 100이하인 정수디이다.

출력
위에서 구하란 걸 구하면 된ㄷ."""

# 정보) 
# (a+b)^2 = a^2+b^2+2ab
# (a+b+c)^2 = a^2+b^2+c^2+2(ab+bc+ac)
N = int(input())
answer = 0
notanswer = 0
nums = list(map(int, input().split(" ")))
answer = sum(nums)*sum(nums)
for i in nums:
    notanswer += (i*i) 

print((answer-notanswer)//2)
