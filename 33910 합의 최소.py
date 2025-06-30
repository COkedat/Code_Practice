"""문제
길이가 
$N$인 정수로 구성된 수열 
$A_1,A_2,...,A_N$이 주어진다.

당신은 아래 연산을 0번 이상 사용하여 수열의 모든 원소들의 합 
$\displaystyle\sum_{i=1}^NA_i$를 최소화하려고 한다.

 
$1$ 이상 
$N-1$ 이하인 정수 
$i$를 선택한 뒤, 
$A_i$의 값을 
$A_{i+1}$로 변경한다.
만들 수 있는 수열의 합의 최솟값을 구해보자.

입력
첫째 줄에 수열의 길이 
$N$이 주어진다.

둘째 줄에 수열의 원소 
$A_1,A_2,\cdots ,A_N$이 공백으로 구분되어 주어진다.

출력
수열의 합의 최솟값을 출력한다.

제한
 
$1\leq N\leq 500\, 000$ 
 
$1\le A_i\le 1\, 000\, 000$ (
$1\le i\le N$)
입력으로 주어지는 수는 모두 정수이다."""

N = int(input())
nums = list(map(int, input().split(" ")))
nums_r = list(reversed(nums))

# 딕셔너리 추가해서 해결
val_dict = {}
for idx, val in enumerate(nums_r):
    if val not in val_dict:
        val_dict[val] = idx
nums_n = sorted(set(nums))
total = 0
curidx = N-1
for i in nums_n:
    idx = val_dict.get(i)
    if(idx > curidx):
        continue
    total += ((curidx - idx + 1) * i)
    curidx = idx - 1
print(total)


# 다른 방법 (더 간단함)
"""
N = int(input())
nums_r = list(map(int, input().split(" ")))[::-1]

for i in range(1, N):
    # 뒤집어서 앞보다 작으면 변경
    if nums_r[i] > nums_r[i - 1]: 
        nums_r[i] = nums_r[i - 1]

print(sum(nums_r))
"""