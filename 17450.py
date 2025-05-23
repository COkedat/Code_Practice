"""문제
남서네 집 앞 편의점에는 각각 S, N, U의 이름이 붙은 총 3가지의 과자를 판다. 진열대에는 한 봉지당 가격과 무게가 안내되어 있다. 같은 종류의 과자끼리는 봉지의 무게가 똑같다.

남서는 오늘 과자를 10봉지 사려고 한다. 편의점의 단골인 남서는 할인 쿠폰 하나를 가지고 있는데, 총 구매 금액이 5,000원 이상일 때 500원을 깎아 주는 쿠폰이다. 구매 금액이 5,000원 미만인 경우에는 할인 쿠폰을 쓸 수 없다. 또한 할인을 여러 번 적용할 수는 없다.

남서는 과자를 고를 때 가성비를 중요하게 생각한다. 남서가 생각하는 가성비란, 총 무게를 총 금액으로 나눈 값이다. 남서는 빨리 과자가 먹고 싶기 때문에, 한 종류의 과자만을 10봉지 골라 사 가려고 한다. 또, 다른 물건은 구매하지 않을 생각이다.

가성비를 다시 한 번 수학적으로 표현하면 다음과 같다.

가성비 = 
과자 10봉지의 무게의 합
쿠폰 사용을 고려했을 때 과자 10봉지를 사는 데 필요한 돈

진열대를 들여다 보던 남서는 신기하게도 세 과자의 가성비가 모두 서로 다르다는 사실을 깨달았다.

남서는 어떤 과자를 사게 될까?

입력
입력은 총 3개의 줄로 이루어지며, 각 줄에는 S, N, U의 순서대로 한 봉지의 가격과 무게가 띄어쓰기를 사이에 두고 주어진다.

모든 입력값은 1 이상 1,000 이하의 정수이다.

세 종류의 과자의 가성비가 서로 다름이 보장된다.

출력
첫 번째 줄에 가장 가성비가 높은 과자의 이름(S 또는 N 또는 U)을 출력한다."""


S = list(map(int, input().split(" ")))
N = list(map(int, input().split(" ")))
U = list(map(int, input().split(" ")))
SNU = [S, N, U]
SNU_str = ['S','N','U']
max_idx=-1
max_num=-1

for i in range(3):
    tmp_c = SNU[i][0]*10 if (SNU[i][0]*10 < 5000) else (SNU[i][0]*10 - 500)
    tmp_w = SNU[i][1]*10
    if (tmp_w / tmp_c) > max_num:
        max_num = tmp_w / tmp_c
        max_idx = i

print(SNU_str[max_idx])

