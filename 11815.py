"""문제
B를 A로 나누었을 때 나머지가 0 이라면 A는 B의 약수라고 할 수 있다. (A > 0, B > 0) 예를 들면 15 의 약수는 1, 3, 5, 15 이다.

주어진 수가 가지는 약수 개수가 홀수인지 짝수인지 판별해보자.

입력
첫 번째 줄에는 전체 테스트 개수 (N) 가 주어진다. (1 ≤ N ≤ 100)

두 번째 줄에는 약수 개수를 판별할 수 (X) 가 주어진다 (1 ≤ X ≤ 10^18).

출력
주어진 수의 약수 개수가 홀수이면 1, 짝수이면 0 을 출력하시오."""

# 아이디어 : 완전제곱수는 약수의 개수가 홀수임
N = int(input())
X = list(map(int, input().split(" ")))
for i in X:
    # i의 제곱근을 구하고 소수 부분을 버림
    # => 그 후 다시 제곱한 수가 i와 일치하는지 확인
    if((int(i ** (1/2)) ** 2) == i):
        print(1, end=" ") # 일치하면 홀수
    else:
        print(0, end=" ") # 일치하지 않으면 짝수