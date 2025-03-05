# 이거 그냥 카운팅용임 별거없음

answer = [0,0,0,0,0,0,0,0,0,0]
for i in range(1,111111+1):
    tmp=list(str(i))
    #while(len(tmp)<4): # 10000이하의 경우는 0붙이기 안함
    #    tmp=['0']+tmp
    answer[0]+=tmp.count("0")
    answer[1]+=tmp.count("1")
    answer[2]+=tmp.count("2")
    answer[3]+=tmp.count("3")
    answer[4]+=tmp.count("4")
    answer[5]+=tmp.count("5")
    answer[6]+=tmp.count("6")
    answer[7]+=tmp.count("7")
    answer[8]+=tmp.count("8")
    answer[9]+=tmp.count("9")
print(f"{answer[0]} {answer[1]} {answer[2]} {answer[3]} {answer[4]} {answer[5]} {answer[6]} {answer[7]} {answer[8]} {answer[9]}")