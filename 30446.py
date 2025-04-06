"""문제
어떤 양의 정수 
$P$에 대해 
$P$를 구성하는 숫자들을 왼쪽부터 적는 경우와 오른쪽부터 적은 결과가 서로 일치할 경우, 
$P$를 회문수(palindrome number)라 한다. 예를 들어 
$1$, 
$101$, 
$12322321$은 모두 회문수이다. 양의 정수 
$n$이 주어졌을 때, 
$n$ 이하의 서로 다른 회문수의 개수를 출력하는 프로그램을 작성하시오. 예를 들어 
$n = 20$ 인 경우, 
$20$ 이하의 회문수는 총 
$10$개 ($1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$, $11$) 존재한다.

입력
입력은 표준입력을 사용한다. 첫 번째 줄에 양의 정수 
$n$ ($1 ≤ n < 10^{10}$) 이 주어진다.

출력
출력은 표준출력을 사용한다. 
$n$ 이하의 서로 다른 회문수의 개수를 한 줄에 출력한다."""
def countPalin(N):
    N = str(N)
    max_len = len(N)
    count = 0

    # 1자리부터 N의 자리수까지의 회문수를 생성
    for length in range(1, max_len + 1):
        # 회문의 앞부분 자리수
        half_len = (length + 1) // 2  
        # 앞부분 -> 시작값과 끝값으로 분리
        # ex) half_len = 5이면 10000 ~ 99999 (앞자리가 0이 되면 안 되므로 10부터 시작해야함)
        start = pow(10, half_len-1) if half_len > 1 else 1
        end = pow(10, half_len)

        # 가능한 모든 앞부분을 돌음
        for half in range(start, end):
            # 반쪽 자리
            half_str = str(half)

            # 짝수 자리) 앞부분 + 앞부분 뒤집어 연결
            if length % 2 == 0:
                palin = int(half_str + half_str[::-1])
            # 홀수 자리) 앞부분 + 앞부분의 마지막 숫자 제외한 부분 뒤집어 연결
            else:
                palin = int(half_str + half_str[-2::-1])

            # 만든 회문수가 N보다 작거나 같다면 카운트
            if palin <= int(N):
                count += 1
            # 작으면 break -> 더 나갈 필요 없음
            else:
                break
    # 리턴
    return count

N = int(input())
print(countPalin(N))





