"""입력
The input is a single line containing a positive integer n ≤ 50 (the length of the code) followed by two strings of length n — the first of these is the code and the second is the guess. Both code and guess are made up of upper-case alphabetic characters.

출력
Output the values of r and s for the given input.
"""

tmp = input().split(" ")
N = int(tmp[0])

code= list(tmp[1])
guess= list(tmp[2])

pop_index=[]
strike = 0
ball = 0

for i in range(N):
    if(code[i]==guess[i]):
        pop_index.append(i)
        strike+=1

pop_index.sort(reverse=True)

for j in pop_index:
    code.pop(j)
    guess.pop(j)

for k in code:
    if(k in guess):
        ball+=1
        guess.remove(k)

print(str(strike)+" "+str(ball))