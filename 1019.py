"""문제
지민이는 전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.

입력
첫째 줄에 N이 주어진다. N은 1,000,000,000보다 (10억) 작거나 같은 자연수이다.

출력
첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 공백으로 구분해 출력한다."""
#그냥 정공법으로 세는 함수
def countPage(N, answer, frontNum=[]):
    #그냥 진짜 정공법임
    for i in range(1,N+1):
        tmp=list(str(i))
        while(len(tmp)<4 and len(frontNum)!=0): # 10000이하의 경우는 0붙이기 안함
            tmp=['0']+tmp
        answer[0]+=(tmp.count("0")+frontNum.count("0"))
        answer[1]+=(tmp.count("1")+frontNum.count("1"))
        answer[2]+=(tmp.count("2")+frontNum.count("2"))
        answer[3]+=(tmp.count("3")+frontNum.count("3"))
        answer[4]+=(tmp.count("4")+frontNum.count("4"))
        answer[5]+=(tmp.count("5")+frontNum.count("5"))
        answer[6]+=(tmp.count("6")+frontNum.count("6"))
        answer[7]+=(tmp.count("7")+frontNum.count("7"))
        answer[8]+=(tmp.count("8")+frontNum.count("8"))
        answer[9]+=(tmp.count("9")+frontNum.count("9"))

# 대충 ~0000 땡처리용 함수
def addZeroPage(answer, frontNum=[]):
    answer[0]+=(4+frontNum.count("0")) # 네자리수 + 앞자리수의 0 개수
    answer[1]+=frontNum.count("1")
    answer[2]+=frontNum.count("2")
    answer[3]+=frontNum.count("3")
    answer[4]+=frontNum.count("4")
    answer[5]+=frontNum.count("5")
    answer[6]+=frontNum.count("6")
    answer[7]+=frontNum.count("7")
    answer[8]+=frontNum.count("8")
    answer[9]+=frontNum.count("9")

# 패턴화된거 넣는 함수
def fillPage(answer, frontNum=[]):
    # 0000~9999는 각각 모두 4000임
    # 앞자리수는 0000~9999까지 총 1만번 반복되기 때문에 10000을 곱해줌
    answer[0]+=(4000+frontNum.count("0")*10000)
    answer[1]+=(4000+frontNum.count("1")*10000)
    answer[2]+=(4000+frontNum.count("2")*10000)
    answer[3]+=(4000+frontNum.count("3")*10000)
    answer[4]+=(4000+frontNum.count("4")*10000)
    answer[5]+=(4000+frontNum.count("5")*10000)
    answer[6]+=(4000+frontNum.count("6")*10000)
    answer[7]+=(4000+frontNum.count("7")*10000)
    answer[8]+=(4000+frontNum.count("8")*10000)
    answer[9]+=(4000+frontNum.count("9")*10000)

N = int(input())
answer = [0,0,0,0,0,0,0,0,0,0]

# 100000까지는 그냥 구해줘도 됨
if(N<=100000): 
    countPage(N, answer)
else: # 그 이상일경우

    # 네자리수가 있을 경우
    if(N%10000!=0): 
        countPage(N%10000, answer, list(str(N//10000)))
        addZeroPage(answer, list(str(N//10000)))
        N=N-(N%10000)-1 # 일단 잔수 제거 ( ~~~9999 됨)

    # 네자리수가 없을 경우 (~~~0000 일경우)
    else: 
        addZeroPage(answer, list(str(N//10000)))
        N=N-(N%10000)-1 #( ~~~9999로 만듦)

    # 9999가 될때까지 빼줌
    while(N>=10000):
        fillPage(answer, list(str(N//10000)))
        N=N-10000
    # 9999는 그냥 카운트, 왜냐면 앞자리수가 없음
    countPage(N, answer)

print(f"{answer[0]} {answer[1]} {answer[2]} {answer[3]} {answer[4]} {answer[5]} {answer[6]} {answer[7]} {answer[8]} {answer[9]}")
        

