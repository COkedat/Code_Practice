"""입력
The first line of input contains an integer N (1 ≤ N ≤ 100), how many pieces of food the children take. 

Each of the following N lines contains the name of a child that took one piece of food. The names will be strings of at most 20 lowercase letters of the English alphabet. 

출력
Output the number of warnings on a single line. """

N = int(input())
order = []
cookies = {}
cnt = 0
answer = 0
for i in range(N):
    M = input()
    order.append(M)
    cookies[M] = 0

for j in range(N):
    if (cnt - cookies[order[j]] < cookies[order[j]]):
        answer += 1
    cnt += 1
    cookies[order[j]] += 1
    
print(answer)