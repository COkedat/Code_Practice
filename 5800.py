"""문제
한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다. 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.

중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 중덕 고등학교에 있는 반의 수 K (1 ≤ K ≤ 100)가 주어진다. 다음 K개 줄에는 각 반의 학생수 N (2 ≤ N ≤ 50)과 각 학생의 수학 성적이 주어진다. 시험 성적은 0보다 크거나 같고, 100보다 작거나 같은 정수이고, 공백으로 나누어져 있다. 

출력
각 반에 대한 출력은 다음과 같이 두 줄로 이루어져 있다.

첫째 줄에는 "Class X"를 출력한다. X는 반의 번호이며 입력으로 주어진 순서대로 1부터 증가한다.
둘째 줄에는 가장 높은 점수, 낮은 점수, 성적을 내림차순으로 정렬했을 때 가장 큰 인접한 점수 차이를 예제 출력과 같은 형식으로 출력한다."""
import sys
N = int(input())
for j in range(N):
    gap=-1
    tmp = list(map(int, sys.stdin.readline().split(" ")))
    tmp.pop(0) # 첫번째 더미 제거
    tmp.sort(reverse=True)
    for i in range(len(tmp)-1):
        if (tmp[i]-tmp[i+1]>gap):
            gap=tmp[i]-tmp[i+1]
    print(f"Class {j+1}")
    print(f"Max {max(tmp)}, Min {min(tmp)}, Largest gap {gap}")
