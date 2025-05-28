#세 참가자의 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬해서 이어 붙인 문자열
#세 참가자 중 성씨를 영문으로 표기했을 때의 첫 글자를 백준 온라인 저지에서 해결한 문제가 많은 사람부터 차례대로 나열한 문자열
N=[]
while True:
    try:
        k = input()
        k = k.split(" ")
        k[0] = int(k[0])
        k[1] = int(k[1])%100
        k[2] = list(k[2])[0]
        N.append(k)
    except:
        break
N_1 = sorted(N, key = lambda x : x[1])
N_2 = sorted(N, key = lambda x : -x[0])

for i in N_1:
    print(i[1],end='')
print()
for i in N_2:
    print(i[2],end='')