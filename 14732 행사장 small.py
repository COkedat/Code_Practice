"""문제
상현이는 국방부 퀘스트를 수행하기 전에 이별 파티를 기획하고 있다. 따라서 파티를 진행하기 위해 행사장을 대여하려고 한다.

이 대여 업체는 전직 프로그래머들만 일하기 때문에 대여 방식이 독특하다. 상현이가 대여 장소를 정하면 그 장소를 완전히 포갤 수 있는 N개의 직사각형을 만든다. 그 후 직사각형의 개수 N과 각 직사각형들의 좌측 하단과 우측 상단의 좌표를 알려준다. N개의 직사각형들은 일부분 혹은 전체가 겹칠 수도 있다.

상현이가 빌린 행사장의 넓이를 구하는 프로그램을 작성하라.

입력
첫째 줄에 직사각형의 개수 N(2 ≤ N ≤ 100)이 주어진다.

이어 N개의 줄에 네 정수 x1, y1, x2, y2(0 ≤ x1 < x2 ≤ 500, 0 ≤ y1 < y2 ≤ 500)가 순서대로 주어진다. 이는 좌측 하단의 좌표 (x1, y1), 우측 상단의 좌표 (x2, y2)이다.

출력
첫째 줄에 상현이가 빌린 행사장의 넓이를 출력하라."""
from sys import stdin
input = stdin.readline
N = int(input())
room = [ [0 for _ in range(501)] for _ in range(501) ]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split(" "))
    for i in range(x1,x2):
        for j in range(y1,y2):
            if(room[i][j] == 0):
                room[i][j] = 1

answer = sum([num.count(1) for num in room])
print(answer)