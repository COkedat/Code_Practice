A=input()
B=input()
answer=""
moum = ["a", "e", "i", "o", "u"]

A_met = False
for i in range(len(A)):
    if(A[i] in moum):
        A_met = True
        answer+=A[i]
    if(A[i] not in moum):
        if A_met:
            break
        else:
            answer+=A[i]  

B_met = False   
for i in range(len(B)):
    if(B[i] in moum):
        B_met = True
        answer+=B[i]
    if(B[i] not in moum):
        if B_met:
            break
        else:
            answer+=B[i]  
            
if (A_met and B_met):
    print(answer)
else:
    print("no such exercise")