"""입력
The first line of the input is a string containing only lowercase latin letters. The string is at most 250 symbols in length.

출력
Output the corrected string in the first line of the output."""

N = list(input())
M = []
prev=""
for i in N:
    if(i != prev):
        M.append(i)
    prev = i
for j in M:
    print(j,end="")