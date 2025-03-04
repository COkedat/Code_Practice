"""문제
세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때, 이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값을 구하고 싶다.

입력
첫째 줄에 빨대의 개수 N이 주어진다. N은 3보다 크거나 같고, 1,000,000보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 빨대의 길이가 한 줄에 하나씩 주어진다. 빨대의 길이는 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 삼각형 세 변의 길이의 합의 최댓값을 출력한다. 만약 삼각형을 만들 수 없으면 -1을 출력한다."""
from sys import stdin
from collections import deque
N = int(input())
straws = []
isTri = False
answer = deque([])
for _ in range(N):
    straws.append(int(stdin.readline()))
straws = deque(sorted(straws))

#초기 3개
answer.appendleft(straws.pop())
answer.appendleft(straws.pop())
answer.appendleft(straws.pop())

# 빨대가 빌때까지
while(len(straws)>0):
    if(answer[0]+answer[1]>answer[2]): # 만약 삼각형 조건이 맞다면 바로 탈출
        isTri = True
        break
    answer.pop()
    answer.appendleft(straws.pop())

if(answer[0]+answer[1]>answer[2]): # 마지막 한번 더 체크
    isTri = True
    
if(isTri):
    print(sum(answer))
else:
    print(-1)