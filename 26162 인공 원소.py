"""문제
원자 번호 43번을 가진 테크네튬은 세계 최초의 인공 방사성 원소이자, 가장 가벼운 방사성 원소이다. 테크네튬의 최초 발견은 특이하게도 자연이 아닌 인공 합성을 통해 이루어졌는데, 원자 번호 42번을 가진 몰리브데넘에 입자를 충돌시키는 방식으로 생성되었다고 한다.

테크네튬의 어떠한 특성이 이러한 인공 합성 과정을 가능하게 했을지 궁금해진 준익이는, 깊은 고심 끝에 소수 두 개의 합으로 나타낼 수 있는 원자 번호에 그 이유가 있을 것이라는 엉뚱한 가설을 내세웠다! 자신의 엄청난 발견에 스스로 감탄한 준익이는, 각 원소가 인공 합성이 가능할지에 대한 여부를 마구 따져보고자 한다. 준익이를 위해 주어진 원자 번호를 가진 원소가 인공 합성이 가능한 원소인지 알아보자!

입력
첫째 줄에 물어볼 원자 번호의 개수 
$N$이 주어진다. (
$1 \le N \le 118$)

이후 
$N$개의 줄에 걸쳐 원자 번호 
$a$가 주어진다. (
$1 \le a \le 118$)

이때 같은 원자 번호는 두 번 이상 주어지지 않는다.

출력
각 원자 번호를 가진 원소가 인공 합성이 가능한 원소라면 Yes, 아니라면 No를 주어진 순서대로 한 줄에 하나씩 출력한다.
"""
import math
m = 118
array = [True for i in range(m + 1)] 
array[0]=False
array[1]=False
#2부터 루트 N까지
for i in range(2, int(math.sqrt(m)) + 1):
    # 숫자 i가 소수라면
    if array[i] == True: 
        j = 2
        # m 보다 작은 i * j는 소수가 아님
        while i * j <= m:
            array[i * j] = False
            j += 1
N = int(input())

def chkArr(N):
    for i in range(2, N+1):
        if(array[i] and array[N-i]):
            return True
    return False

for _ in range(N):
    tmp = int(input())
    if(chkArr(tmp)):
        print("Yes")
    else:
        print("No")