"""문제
크레이지 아케이드를 하면서 폭탄을 피하려고 한다. 게임을 하는 곳은 10×10 크기의 배열로 나타낼 수 있고, 폭탄이 있는 칸은 o, 없는 칸은 x로 나타낸다. 폭탄이 터질 때, 폭탄과 같은 행 또는 같은 열에 있다면, 물방울에 갇히게 된다.

예를 들어, 아래와 같은 배열에서 폭탄이 터지게 되면, (4,3)에 있어야 물방울에 갇히는 것을 피할 수 있다.

x x x o
o x x x
x o x x
x x x x
위치와 게임판이 주어졌을 때, 물방울에 갇히지 않기 위해 움직여야 할 최소 이동 횟수를 구해보자. 한 번에 한 칸 가로 또는 세로로 이동할 수 있다. 폭탄 위를 지나갈 수 있으며, 움직이지 않아도 된다면 0을 출력한다.

입력
첫째 줄에 플레이어의 위치 (r, c)가 주어진다. 배열의 가장 윗 행은 1번 행, 가장 왼쪽 열은 1번 열이다. 둘째 줄부터 10개의 줄에 걸쳐서 게임판의 상태가 주어진다. 물방울에 갇히지 않는 경우만 입력으로 주어진다.

출력
첫째 줄에 최소 이동 횟수를 출력한다."""

def makeLine(coor, i, j):
    for x in range(10):
        if (coor[i][x]!='o'):
            coor[i][x]='O'
        if (coor[x][j]!='o'):
            coor[x][j]='O'

distance = 9999

# 현재 위치
curP = list(map(int, input().split(" ")))
coor = []

for i in range(10):
    tmp = list(input())
    coor.append(tmp)

for i in range(10):
    for j in range(10):
        if(coor[i][j]=="o"):
            makeLine(coor,i,j)

for i in range(10):
    for j in range(10):
        if(coor[i][j]=="x"):
            tmp = abs(i-(curP[0]-1))+abs(j-(curP[1]-1))
            if (tmp<distance):
                distance = tmp

print(distance)