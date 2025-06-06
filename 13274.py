"""지훈이는 수열을 좋아한다. 지금 지훈이는 size 가 N 인 수열을 가지고 놀고 있다. 
지훈이는 K 개의 쿼리에 따라 수열을 변화시킬 것인데, 쿼리의 형식 및 작업 과정은 다음과 같다.

L R X : 수열을 오름차순으로 정렬한 결과를 A[1], A[2], … , A[N]이라 하자. 우선 A[L], A[L+1], … , A[R]에 X 만큼 더한다. 그 결과 수열을 다시 오름차순으로 정렬한다.
쿼리들을 순서대로 모두 수행한 후의 수열을 출력하라.

입력
첫째 줄에 N 과 K 가 띄어쓰기로 구분되어 주어진다. (1 ≤ N ≤ 100000, 1 ≤ K ≤ 1000)

둘째 줄에 절댓값이 1018 이하인, 수열을 이루는 N 개의 정수가 주어진다.

셋째 줄부터 K+2 번째 줄까지 쿼리 L R X 가 주어진다. (1 ≤ L ≤ R ≤ N, |X| ≤ 109)

출력
쿼리들을 순서대로 모두 수행한 후의 수열을 출력한다."""

N, K = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
nums.sort()

for _ in range(K):
    L, R, X = map(int, input().split(" "))

    # 해당 범위만 계산해서 치환
    nums[L-1:R] = list(map(lambda x : x+X, nums[L-1:R]))

    nums.sort() # 오름차순 정렬

for i in nums:
    print(i, end=' ')