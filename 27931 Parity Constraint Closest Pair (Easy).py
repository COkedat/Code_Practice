"""문제
수직선상에 좌푯값이 서로 다른 
$N$개의 격자점이 있다. 서로 다른 두 점의 거리 중 짝수인 최솟값과 서로 다른 두 점의 거리 중 홀수인 최솟값을 각각 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 점의 개수를 나타내는 양의 정수 
$N$이 주어진다.

두 번째 줄에는 각 점의 좌표를 나타내는 정수 
$N$개가 공백으로 구분되어 주어진다.

출력
첫 번째 줄에 서로 다른 두 점의 거리 중 짝수인 최솟값과 서로 다른 두 점의 거리 중 홀수인 최솟값을 공백으로 구분하여 출력한다. 단, 해당하는 거리가 없는 경우 -1을 출력한다.

제한
입력으로 주어지는 모든 좌푯값의 절댓값은 
$10^9$보다 작거나 같다.
두 점이 같은 좌표를 가지는 경우는 없다."""
N = int(input())
dots = list(map(int,input().split(" ")))
dots.sort()
# 대충 최대값
min_odd = 2*pow(10,9)+2
min_even = 2*pow(10,9)+3

# 가장 마지막에 나온 홀짝 (처음엔 없으므로 None)
last_odd = None
last_even = None

for i in dots:
    if (i % 2 != 0): # 홀수일 경우
        if(last_even != None):
            # 홀수 i - 마지막 짝(=홀수 길이)과 현재 최소 홀수 길이와 비교
            min_odd = min(min_odd, i-last_even)
        if(last_odd != None):
            # 홀수 i - 마지막 홀(=짝수 길이)과 현재 최소 짝수 길이와 비교
            min_even = min(min_even, i-last_odd)
        last_odd = i
    else: # 짝수일 경우
        if(last_odd != None):
            # 짝수 i - 마지막 홀(=홀수 길이)과 현재 최소 홀수 길이와 비교
            min_odd = min(min_odd, i-last_odd)
        if(last_even != None):
            # 짝수 i - 마지막 짝(=짝수 길이)과 현재 최소 짝수 길이와 비교
            min_even = min(min_even, i-last_even)
        last_even = i

# 마지막에 홀짝 이상여부 체크 이상있으면 변한게 없는거니까 -1 처리
if min_odd % 2 == 0:
    min_odd = -1
if min_even % 2 != 0:
    min_even = -1  

# 출력
print(f"{min_even} {min_odd}")