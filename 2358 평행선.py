"""문제
평면에 n개의 점이 있다. 그중 두 개 이상의 점을 지나면서 x축 또는 y축에 평행한 직선이 몇 개인지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 각 점의 좌표가 주어진다. 같은 좌표가 여러 번 주어질 수 있으며, 그런 경우 서로 다른 점으로 간주한다. 좌표는 절댓값이 231보다 작은 정수이다.

출력
첫째 줄에 답을 출력한다."""
from sys import stdin
input = stdin.readline
N = int(input())
cnt = 0
x = {}
y = {}
chk_x = []
chk_y = []

# x축과 y축은 따로이기 때문에 분리해서 저장
for _ in range(N):
    nx, ny = map(int, input().split(" "))
    chk_x.append(nx)
    chk_y.append(ny)
    # 이미 뭐가 있다면 1 더함
    if (nx in x):
        x[nx]+=1
    # 없다면 해당 라인내 점 개수는 단 1개
    else:
        x[nx]=1
    # 이미 뭐가 있다면 1 더함
    if (ny in y):
        y[ny]+=1
    # 없다면 해당 라인내 점 개수는 단 1개
    else:
        y[ny]=1

# 점들 중복 제거
chk_x=set(chk_x)
chk_y=set(chk_y)

# 한 직선당 점 2개 이상 존재 여부 체크 및 카운트
for i in chk_x:
    if(x[i]>1):
        cnt+=1
for i in chk_y:
    if(y[i]>1):
        cnt+=1

# 정답 출력
print(cnt)