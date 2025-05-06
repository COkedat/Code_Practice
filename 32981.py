"""문제
최근에 치토는 찐 Even Number라는 독특한 수를 정의했다. 찐 Even Number란 
$N$자리 음이 아닌 정수에서 모든 자릿수가 
$\{0, 2, 4, 6, 8\}$로만 이루어진 수를 의미한다. 이때, 
$0$을 제외하고 
$0246$과 같이 
$0$으로 시작하는 수는 고려하지 않는다. 예를 들어, 
$468$과 
$660$은 찐 Even Number이지만 
$14$나 
$567$은 아니다.

민성이는 찐 Even Number에 대해 호기심이 생겨 치토에게 
$Q$개의 질문을 하려 한다. 질문의 형태는 다음과 같다.

 
$N$: 음이 아닌 
$N$자리 정수 중, 서로 다른 찐 Even Number의 개수
치토를 도와 
$Q$개의 질문에 대한 답을 구해보자.

입력
첫 번째 줄에 질문 개수인 양의 정수 
$Q$가 주어진다. 
$(1 \leq Q \leq 100\,000)$ 

두 번째 줄부터 
$Q$개의 줄에 걸쳐 치토에게 질문할 양의 정수 
$N$이 주어진다. 
$(1 \leq N \leq 10^7)$ 

출력
 
$Q$줄에 걸쳐 치토가 답변하는 수를 
$10^9+7$로 나눈 나머지를 각 줄에 하나씩 출력한다."""
# dfs는 아닌듯
"""import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
Q = int(input())

def dfs_find(N, cnt, path):
    if len(path)==N:
        cnt[0] += 1
        return
    for i in range(0,9,2):
        if(len(path)==N-1 and i==0):
            continue
        else:
            dfs_find(N, cnt, path + [i])

for _ in range(Q):
    N = int(input())
    cnt = [0]
    dfs_find(N, cnt, [])
    print(cnt[0]+1 % (pow(10,9) + 7) )"""

"""from sys import stdin
input = stdin.readline
Q = int(input())
mod = (pow(10,9) + 7)
max_num = 2
dp = [0 for _ in range(10000001)]
dp[1] = 5
dp[2] = 20

for _ in range(Q):
    N = int(input())
    if(max_num < N):
        for i in range(max_num+1, N+1):
            dp[i] = dp[i - 1] * 5 % mod
    print(dp[N])"""


from sys import stdin
input = stdin.readline
Q = int(input())
mod = (pow(10,9) + 7)

def calc(N):
    res = 1
    base = 5
    #N-=1
    while (N > 0):
        if (N % 2 == 1):
            res = (res * base) % mod
            base = (base * base) % mod
        N //= 2 
    return res 

for _ in range(Q):
    N = int(input())
    if (N == 1):
        print(5)
    else:
        print((calc(N) * 4) % mod)