# 입력
row, col = map(int, input().split(" "))
chess = []
answer = 0
for i in range(row):
    tmp = input().split(" ")
    for i in tmp:
        answer += i.count("9")
    chess.append(tmp)
max_num = 0

for i in range(row):
    tmp = 0
    for j in range(col):
        tmp += chess[i][j].count("9")
    if (tmp > max_num):
        max_num = tmp

for i in range(col):
    tmp = 0
    for j in range(row):
        tmp += chess[j][i].count("9")
    if (tmp > max_num):
        max_num = tmp

answer -= max_num
print(answer)
