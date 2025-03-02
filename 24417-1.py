"""문제
오늘도 서준이는 동적 프로그래밍 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

피보나치 수 재귀호출 의사 코드는 다음과 같다.

fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
입력
첫째 줄에 n(5 ≤ n ≤ 2 × 108)이 주어진다.

출력
코드1 코드2 실행 횟수를 1,000,000,007로 나눈 나머지를 한 줄에 출력한다."""

modman = int(1e9) + 7

def matrix_multi(A, B): #행렬 A와 B를 곱함
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % modman,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % modman],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % modman,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % modman]]

def matrix_power(A, n): #행렬 A를 n번 거듭제곱
    result = [[1, 0], [0, 1]]  # 단위 행렬
    while n:
        if n % 2:
            result = matrix_multi(result, A)
        A = matrix_multi(A, A)
        n //= 2
    return result

def fib1(n): #O(log N)으로 피보나치 수를 계산
    if n <= 2:
        return 1
    F = [[1, 1], [1, 0]]
    result = matrix_power(F, n - 1)
    return result[0][0]  # F(n) 값 반환

N = int(input())

fib1_val = fib1(N)  # F(N)
fib2 = (N-2) % modman  # 재귀 호출 횟수

print(f"{fib1_val} {fib2}")