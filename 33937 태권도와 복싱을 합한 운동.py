A=input()
B=input()
answer=""
moum = ["a", "e", "i", "o", "u"]
cnt = 0
A_met = -1
for i in range(len(A)):
    if(A[i] in moum):
        if i == len(A)-1:
            A_met = -1
            break
        A_met = i+1
        answer+=A[i]
    if(A[i] not in moum):
        if A_met!=-1:
            break

B_met = -1 
for i in range(len(B)):
    if(B[i] in moum):
        if i == len(B)-1:
            A_met = -1
            break
        B_met = i+1
        answer+=B[i]
    if(B[i] not in moum):
        if B_met!=-1:
            break


answer=A[:A_met]+B[:B_met]
if (A_met!=-1 and B_met!=-1):
    print(answer)
else:
    print("no such exercise")