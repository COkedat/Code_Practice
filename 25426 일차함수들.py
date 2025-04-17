"""문제
 
$f(x) = ax + b$형태의 일차함수가 
$N$개 있다. 
$i$번째 함수는 
$f_i(x) = {a_i}x + {b_i}$로 표현된다.

이 함수들 각각의 
$x$에 
$1$부터 
$N$까지의 서로 다른 정수 
$N$개를 하나씩 대입하여 만들 수 있는 
$f(x)$들의 합의 최댓값을 구해보자.

구체적으로는, 길이 
$N$의 순열 
$x_1, x_2, ... x_N$을 적절히 정해 
$\sum_{i=1}^N {a_i}{x_i}+{b_i}$의 값을 최대화하여라.

입력
첫째 줄에 일차함수의 개수 
$N$이 주어진다. 
$(1≤N≤100,000)$ 

둘째 줄부터 
$N$줄에 걸쳐 
$i$번째 일차함수를 나타내는 두 정수 
$a_i, b_i$가 공백으로 구분되어 입력된다. 
$(0≤a_i, b_i≤ 10^9)$ 

출력
첫째 줄에 문제의 답을 출력한다."""

from sys import stdin
input = stdin.readline

N = int(input())
nums = []
for _ in range(N):
    A, B=map(int,input().strip().split())
    nums.append([A,B])

nums.sort()
answer = 0
for i in range(N):
    answer += nums[i][0]*(i+1)+nums[i][1]

print(answer)
