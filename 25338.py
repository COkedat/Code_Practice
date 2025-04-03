"""문제
시루는 가을에 입을 바지를 미리 사기 위해 백화점에 왔다. 다리가 길고 저체중인 시루는 길이가 맞는 바지를 사면 허리가 너무 크고, 허리가 맞는 바지를 사면 길이가 짧아서 잘 맞는 바지를 찾지 못하고 있다.

길이가 맞는 바지를 산 다음 허리둘레를 수선을 하거나 허리띠를 하면 되지만, 수선하는 것은 귀찮고 허리띠를 불편해하는 시루는 멋진 아이디어를 생각해냈다. 허리가 조금 크고 길이가 조금 짧은 바지를 산 다음, 허리가 아닌 엉덩이에 바지를 걸치는 방식으로 입는 것이다.

지면에서 
$x$ 만큼 떨어진 시루의 하체 둘레는 
$f(x) = \max(a(x-b)^2+c, d)$로 계산할 수 있다. 예를 들어 
$f(x) = \max(-0.1(x-50)^2+10, 6)$이라고 하면, 시루가 엎드려 있을 때 하체는 다음과 같은 형태이다.

시루는 백화점에서 
$n$개의 바지를 골랐다. 
$i$번째 바지의 허리둘레는 
$u_i$, 길이는 
$v_i$이다. 바지를 위에서부터 내려가는 방식으로 허리둘레가 시루의 하체 둘레와 딱 맞도록 바지를 입었을 때, 바지가 끌리지 않으면서 끝부분의 높이가 지면과 일치하는지 확인해 보자. 바지의 허리 부분은 시루의 하체에서 둘레가 가장 큰 위치보다 높거나 같은 곳에서만 걸린다.

입력
첫째 줄에 시루의 하체 둘레를 의미하는 네 정수 
$a, b, c, d$가 공백으로 구분되어 주어진다. (
$-10 \leq a \leq -1$, 
$1 \leq b \leq 10\,000$, 
$1 \leq d < c \leq 10\,000$)

둘째 줄에 바지의 개수 
$N$이 주어진다. (
$1 \leq N \leq 100\,000$)

셋째 줄부터 
$N$개의 줄에 걸쳐, 
$i$번째 줄에 
$i$번째 바지의 둘레와 길이를 의미하는 두 정수 
$u_i, v_i$가 공백으로 구분되어 주어진다. (
$d < u_i \leq c$, 
$b \leq v_i \leq 10\,000$)

출력
바지가 땅에 끌리지 않고, 바지의 끝부분의 높이가 지면과 일치하는 바지의 개수를 출력한다."""
from sys import stdin
input = stdin.readline
A, B, C, D = map(int,input().strip().split(" "))
N = int(input())
cnt = 0
for _ in range(N):
    # 둘레, 길이
    u, v = map(int,input().strip().split(" "))

    f = max(A*pow(v-B,2)+C,D)
    if(f == u and v >= B):
        cnt+=1
print(cnt)

