"""
문제
정수론(수학)에서, 세 개의 소수 문제(3-primes problem) 는 다음과 같은 추측을 말한다.

'5보다 큰 임의의 홀수는 정확히 세 개의 소수들의 합으로 나타낼 수 있다. 물론 하나의 소수를 여러 번 더할 수도 있다.'

예를 들면,

7 = 2 + 2 + 3
11 = 2 + 2 + 7
25 = 7 + 7 + 11
5보다 큰 임의의 홀수를 입력받아서, 그 홀수가 어떻게 세 소수의 합으로 표현될 수 있는지 (또는 불가능한지) 알아보는 프로그램을 작성하시오.

입력
첫째 줄에 T(Test Case의 수를 의미함)가 주어진다.

입력은 T개의 Test Case로 이루어진다.

각 Test Case는 하나의 정수 K (7 ≤ K < 1,000, K는 홀수)로 구성된다.

출력
T줄에 걸쳐서, 각 줄에 K가 어떻게 세 소수의 합으로 표현되는지 출력해야 한다.

가능하다면 그 세 소수를 오름차순 정렬하여 출력하면 된다.

여러 개의 답이 가능하다면 그 중 하나만 출력하면 되고, 만약 불가능하다면 0을 출력한다."""



import math
primes = []
num = 1000
array = [True for i in range(num + 1)] 
for i in range(2, int(math.sqrt(num)) + 1):
    if array[i] == True: 
        j = 2
        while i * j <= num:
            array[i * j] = False
            j += 1
for i in range(2, len(array)):
    if (array[i]):
        primes.append(i)

def findPrimes(N, p):
    answer = [-1]
    for i in p:
        for j in p:
            for k in p:
                if(i+j+k==N):
                    answer = [k,j,i]
                    break
    return answer


T = int(input())
lis = []
for _ in range(T):
    N = int(input())
    lis.append(N)

for j in lis:
    answer = findPrimes(j, primes)
    if (answer[0] != -1):
        print(f"{answer[0]} {answer[1]} {answer[2]}")
    else:
        print(0)

    