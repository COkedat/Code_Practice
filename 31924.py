"""문제
$N \times N$ 크기의 격자판을 준비하였다. 격자판의 각 칸에는 알파벳 대문자가 한 글자씩 적혀있다. 특별상은 이 격자판에서 가장 많은 MOBIS를 찾은 사람에게 주어지는데, MOBIS를 찾는 것은 다음의 규칙을 따른다.

격자 위의 임의 위치에서 시작하여 상, 하, 좌, 우, 대각선의 8방향 중 한 방향으로 격자에 적힌 글자들을 차례로 5개 이어 붙였을 때, 이어 붙인 글자가 MOBIS여야 한다.
현빈이는 어떻게든 특별상의 주인공이 되고 싶다. 현빈이를 도와 주어진 격자판에서 MOBIS를 최대 몇 번 찾을 수 있는지 구해보자.

입력
첫 번째 줄에 정수 
$N$이 주어진다. 
$(1 \leq N \leq 100)$ 

두 번째 줄부터 
$N+1$번째 줄까지, 현대모비스가 준비한 격자판의 정보가 주어진다. 각 줄은 
$N$개의 알파벳 대문자로 이루어져 있다.

출력
주어진 격자판에서 찾을 수 있는 MOBIS의 개수를 출력한다."""


#dir->0 모든방향
#          상하 좌우
#            i  j
#dir->1 좌상 -1 -1
#dir->2 상   -1 0
#dir->3 우상 -1 +1
#dir->4 우   0  +1
#dir->5 우하 +1 +1
#dir->6 하   +1 0
#dir->7 좌하 +1 -1
#dir->8 좌   0  -1
mobis = ("M","O","B","I","S")
def isValid(grid, i, j, cnt):
    #범위 벗어났다면
    if(i<0 or i>=len(grid) or j<0 or j>=len(grid)):
        return False
    #다르다면
    if(grid[i][j]!=mobis[cnt]):
        return False
    return True
    
def findMOBIS(grid, i, j, cnt, dir):
    if(cnt!=0 and not isValid(grid, i, j, cnt)):
        return 0
    if(cnt==4 and grid[i][j]=="S"):
        return 1
    num = 0
    if dir==0:
        num += findMOBIS(grid, i-1, j-1, cnt+1, 1) #1
        num += findMOBIS(grid, i-1, j, cnt+1, 2) #2
        num += findMOBIS(grid, i-1, j+1, cnt+1, 3) #3
        num += findMOBIS(grid, i, j+1, cnt+1, 4) #4
        num += findMOBIS(grid, i+1, j+1, cnt+1, 5) #5
        num += findMOBIS(grid, i+1, j, cnt+1, 6) #6
        num += findMOBIS(grid, i+1, j-1, cnt+1, 7) #7
        num += findMOBIS(grid, i, j-1, cnt+1, 8) #8
    else:
        if(dir==1):
            num += findMOBIS(grid, i-1, j-1, cnt+1, dir)
        elif(dir==2):
            num += findMOBIS(grid, i-1, j, cnt+1, dir)
        elif(dir==3):
            num += findMOBIS(grid, i-1, j+1, cnt+1, dir)
        elif(dir==4):
            num += findMOBIS(grid, i, j+1, cnt+1, dir)
        elif(dir==5):
            num += findMOBIS(grid, i+1, j+1, cnt+1, dir)
        elif(dir==6):
            num += findMOBIS(grid, i+1, j, cnt+1, dir)
        elif(dir==7):
            num += findMOBIS(grid, i+1, j-1, cnt+1, dir)
        elif(dir==8):
            num += findMOBIS(grid, i, j-1, cnt+1, dir)
    return num

answer = 0

N = int(input())
grid = []
for i in range(N):
    tmp = list(input())
    grid.append(tmp)

for i in range(N):
    for j in range(N):
        if(grid[i][j]=="M"):
            answer += findMOBIS(grid,i,j,0,0)
        
    
print(answer)
