"""문제
폴리매스 왕국의 사람들은 불의 돌을 이용해 불꽃놀이를 합니다. 오늘의 불꽃놀이는 
$N$개의 폭죽 더미를 이용할 예정입니다.

당신은 아래 작업을 정확히 
$N-2$번 반복해서 폭죽을 터뜨리려고 합니다.

양 끝 폭죽 더미를 제외한 폭죽 더미를 하나 고릅니다.
해당 폭죽 더미의 폭죽을 모두 터뜨립니다.
폭발한 폭죽 더미는 사라지고, 양 옆으로 가장 가까운 폭죽 더미의 높이가 1씩 감소합니다.
불꽃놀이가 끝나고 나면 두 개의 폭죽 더미만이 남습니다. 한 번 불꽃놀이에 사용한 폭죽 더미는 재사용이 불가능하기 때문에, 남은 두 폭죽 더미의 높이 중 더 큰 값을 최소화하려고 합니다. 이 값을 찾는 프로그램을 작성해 봅시다.

입력
첫 줄에는 폭죽 더미의 개수 
$N$이 주어집니다. 다음 줄에는 각 폭죽 더미의 높이 
$A_1, A_2, \cdots, A_N$이 주어어집니다.

출력
마지막 두 폭죽 더미 중 더 높은 것의 높이의 최솟값을 출력합니다."""

"""
# 그냥 정석?
N = int(input())
firecrackers = list(map(int, input().split(" ")))
# N-2번 반복
# 양 끝의 길이 비교후 시작
for _ in range(1, len(firecrackers)-1):
    if(firecrackers[0]>firecrackers[-1]):
        firecrackers[0]-=1
        firecrackers[2]-=1
        firecrackers.pop(1)
    else:
        firecrackers[-1]-=1
        firecrackers[-3]-=1
        firecrackers.pop(-2)
print(max(firecrackers))"""


# 효율적인 방법?
## 양끝 폭죽을 제외한 폭죽 개수 입력
N = int(input()) - 2

## 폭죽 길이들 입력
firecrackers = list(map(int, input().split(" ")))

## 양끝 저장
left = firecrackers[0]
right = firecrackers[-1]

## 왼쪽 끝이 오른쪽 끝보다 길 경우 SWAP
if (left > right):
    left, right = right, left

## 오른쪽 끝 - N이 왼쪽보다 길 경우 그거 출력 (더 높은 것의 최소값)
if right-N > left:
    print(right-N)

## 왼쪽이 더 길다면 (더 비교해야한다면)
else:
    # N에서 양 높이의 차이만큼 뺌 -> left에서만 빠지는 횟수
    tmp = N - (right-left)
    # 왼쪽에서 나머지와 몫만큼 뺀 값을 출력 -> 균등분배와 최소값을 위함
    print(left-tmp//2-tmp%2)