"""문제
외계인 윤이는 지구를 정복하고자 세계의 중심 도시인 울산을 침략했다. 울산에는 
$N$개의 빌딩이 일렬로 늘어서 있고, 왼쪽에서 
$i$번째 건물의 높이는 
$h_i$이다.

윤이는 울산을 파괴하기 위해 다음과 같은 계획을 세웠다. 윤이는 매일 UFO를 타고 울산의 상공을 가르며 가장 높이가 높은 빌딩에 레이저를 발사할 것이다. 레이저에 맞은 빌딩은 높이가 
$1$ 낮아진다. 만약 그 날에 가장 높이가 높은 빌딩이 여러 개라면, 해당하는 모든 빌딩에 레이저를 발사한다. 만약 이미 모든 빌딩의 높이가 
$0$이 되었다면, 윤이는 더 이상 레이저를 발사하지 않는다.

윤이는 지금까지 
$D$일 동안 계획을 착실하게 수행해 왔다. 윤이가 
$D$일 동안 레이저를 발사한 총 횟수를 구하시오.

입력
첫 번째 줄에 건물의 개수 
$N$과 윤이가 계획을 수행한 날의 수 
$D$가 공백으로 구분되어 주어진다. (
$1\le N\le 300\ 000$, 
$1\le D\le 300\ 000$)

두 번째 줄에 건물의 높이를 나타내는 
$N$개의 정수 
$h_i$가 공백으로 구분되어 주어진다. (
$1\le h_i\le 300\ 000$)

출력
윤이가 
$D$일 동안 레이저를 발사한 총 횟수를 출력한다. (32비트 정수 범위를 넘을 수 있음에 유의하라.)"""


from sys import stdin
input = stdin.readline
N, D = map(int, input().split(" "))
H = list(map(int, input().split(" ")))
dict, cnt = {}, 0
for i in H:
    try: dict[i] += 1
    except KeyError: dict[i] = 1
m = max(list(dict.keys()))
for _ in range(D):
    if m==0:
        break
    cnt += dict[m]
    try: dict[m-1] += dict[m]
    except KeyError: dict[m-1] = dict[m]
    m-=1
print(cnt)

