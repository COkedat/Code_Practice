def getRow(str):
    binlist=[]
    str_tmp = list(map(int, str.split(":")))
    for i in str_tmp:
        binlist.append(bin(i)[2:].zfill(6))
    result = ""
    for i in binlist:
        result+=i
    return result

def getCol(str):
    binlist=[]
    str_tmp = list(map(int, str.split(":")))
    for i in str_tmp:
        binlist.append(bin(i)[2:].zfill(6))
    result = ""
    for i in range(6):
        result+=(binlist[0][i]+binlist[1][i]+binlist[2][i])
    return result


N = int(input())
for _ in range(N):
    time = input()
    print(f"{getCol(time)} {getRow(time)}")