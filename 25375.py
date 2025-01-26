"""
a = gcd(x,y)
b = x+y

a는 x와 y를 나누어 떨어트림
따라서 x+y도 나누어떨어트림


입력
첫째 줄에 질의의 개수 
$Q$가 주어진다.

둘째 줄부터 
$Q$개의 줄에 걸쳐 정수 
$a,b$가 공백으로 구분되어 주어진다.

출력
질의마다 조건에 맞는 자연수 쌍이 존재하면 
$1$, 그렇지 않으면 
$0$을 줄마다 출력한다."""

#정수론이라 난 어렵다
import sys
N = int(input())
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    a, b = tmp[0], tmp[1]
    if(b%a==0 and a*2<=b):
        print(1)
    else:
        print(0)
        

