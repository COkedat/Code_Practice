"""문제
미래를 예측하는 능력이 있는 정균이는 앞으로 
$N$일간 ANA 회사의 주가가 어떻게 변하는지 정확히 예측할 수 있다. 정균이는 예측한 결과를 바탕으로 ANA 회사의 주식 한 주를 적당한 시점에 사고 적당한 시점에 팔아서 최대한의 이득을 얻으려고 한다.

ANA 회사의 앞으로 
$N$일간의 주가를 
$a_1, a_2, ..., a_N$이라고 하자. 정균이가 
$i$번째 날에 주식을 사고, 
$j$번째 날에 판다면 
$a_j - a_i$만큼의 이득을 얻을 수 있다. 정균이는 자금이 넉넉하기 때문에 주가가 아무리 높아도 주식을 살 수 있고, 상황이 여의치 않을 경우 사자마자 바로 팔 수도 있다.

앞으로 
$N$일간 ANA 회사의 주가가 주어졌을 때, 정균이가 주식 한 주를 적당한 시점에 사고 적당한 시점에 팔아서 얻을 수 있는 최대 이득은 얼마일까?

입력
첫째 줄에 정수 
$N(1 \le N \le 200\ 000)$이 주어진다.

두 번째 줄에 정수 
$a_1, a_2, ..., a_N$이 주어진다. 
$a_i(1 \le a_i \le 10^9)$는 
$i$번째 날의 ANA 회사의 주가이다.

출력
ANA 회사의 주식 한 주를 적당한 시점에 사고 적당한 시점에 팔아서 얻을 수 있는 최대 이득을 출력한다."""

# 우왔 또 시간초과어택이
N = int(input())
num_list = list(map(int, input().split(' ')))

benefit, answer = 0, 0

#미리 뒤집어줌
num_list.reverse()

#뒤집은 리스트로 for문
for i in range(N):
    benefit = max(benefit, num_list[i]) # 최고가를 찾아줌, 현재가 가장 크다면 현행 유지
    answer = max(answer,benefit-num_list[i]) # 현재 최대 이득과 최고가와 현재 최고가-현재값중에 더 큰거 고름 = 최대 이득, 현재 최대 이득이 가장 크다면 현행유지

print(answer)
