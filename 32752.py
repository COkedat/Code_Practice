"""문제
길이가 
$N$인 정수열 
$A$가 주어진다. 다음 조건을 만족하면 
$A$는 단조증가하는 수열이다.

 
$1 \le i < j \le N$을 만족하는 모든 
$(i, j)$에 대해 
$A_i \le A_j$ 
 
$A$의 
$L$번째 원소부터 
$R$번째 원소의 순서를 임의로 재배치했을 때 단조증가하는 수열로 만들 수 있는지 확인해 보자.

입력
첫 번째 줄에 
$N$, 
$L$, 
$R$이 공백으로 구분되어 주어진다.

두 번째 줄에 
$A_1$, 
$A_2$, 
$A_3$, 
$\cdots$, 
$A_N$이 공백으로 구분되어 주어진다.

출력
첫 번째 줄에 
$A$를 단조증가하는 수열로 만들 수 있다면 1을, 없다면 0을 출력한다.

제한
 
$1 \le N \le 100\,000$ 
 
$1 \le L \le R \le N$ 
 
$1 \le A_i \le 10^9$ """

def chkParty(nums, L, R):
    # 해당 범위 추출해서 정렬
    tmp = nums[L-1:R]
    tmp.sort()

    # 정렬한거 다시 합침
    tmp_chk = nums[:L-1] + tmp + nums[R:]

    # 모두 순서대로면 True, 아니면 False
    for i in range(1,len(tmp_chk)):
        if(tmp_chk[i-1]>tmp_chk[i]):
            return False
    return True

inp = list(map(int, input().split(" ")))
N = inp[0]
L = inp[1]
R = inp[2]
nums = list(map(int, input().split(" ")))

if(chkParty(nums,L,R)):
    print(1)
else:
    print(0)

