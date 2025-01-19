"""
요율 105.6원/kWh

입력
첫 번째 줄에 질문의 수 
Q가 주어집니다.

다음 Q개의 줄에 a와 
m이 공백으로 구분되어 주어집니다. 해당 질문은 아래를 의미합니다.

가희가 소비 전력이 
a W인 컴퓨터를 이번 달에 총 
m분 사용하였을 때, 컴퓨터가 사용한 전력량에 대한 전기 요금은 얼마인가요?
출력
Q개의 줄에, 질문의 정답을 출력해 주세요."""

from math import floor
N = int(input())
for i in range(N):
    tmp = list(map(int, input().split(" ")))
    answer = floor(0.1056 * tmp[0] * tmp[1] / 60.0)
    print(answer)