"""문제
준석이의 수학선생님은 간단한 수학 문제를 숙제로 내셨다. 그 문제는 어떤 자연수 N이 주어지면 N 이하의 3 또는 7의 양의 배수를 모두 더한 값을 구하는 문제다. 
그러나 숫자를 손가락과 발가락으로 밖에 셀 줄 모르는 준석이는 N이 커지자 문제를 풀지 못했다. 준석이를 위해 우리가 정답을 구해주자. 문제는 중복될 수 있다.

입력
첫째 줄에는 문제의 수를 나타내는 T가 주어진다 (1 ≤ T ≤ 100,000)

그 다음 줄에 빈 칸으로 구분하여 T개의 자연수 N이 주어진다. (10 ≤ N ≤ 80,000)

출력
각 문제마다 답을 출력한다. 출력은 개행으로 구분한다."""
def print37(num):
    threeN = num//3
    sevenN = num//7
    toN = num//21
    sum = (threeN * (threeN+1) // 2) * 3 + (sevenN * (sevenN+1) // 2) * 7 - (toN * (toN+1) // 2) * 21
    print(sum)
T = int(input())
N = list(map(int,input().split(" ")))
for i in N:
    print37(i)