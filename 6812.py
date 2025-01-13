"""
1300 in Ottawa (0)
1000 in Victoria (-3)
1100 in Edmonton(-2)
1200 in Winnipeg (-1)
1300 in Toronto (0)
1400 in Halifax (+1)
1430 in St. John's (+1 and 30)
"""
def makeTime(time_list, plus, hour, min):
    answer=""
    if len(time_list)==4:
        oHour = int(time_list[0]+time_list[1])
        oMin = int(time_list[2]+time_list[3])
    elif len(time_list)==3:
        oHour = int(time_list[0])
        oMin = int(time_list[1]+time_list[2])
    elif len(time_list)==2:
        oHour = 0
        oMin = int(time_list[0]+time_list[1])
    elif len(time_list)==1:
        oHour = 0
        oMin = int(time_list[0])
    elif len(time_list)==0:
        oHour = 0
        oMin = 0

    if (plus):
        oMin += min
        oHour += hour
        if oMin >= 60:
            oMin -= 60
            oHour += 1
        if oHour >= 24:
            oHour -=24
    else:
        oMin -= min
        oHour -= hour
        if oMin < 0:
            oMin = 60 + oMin
            oHour += 1
        if oHour < 0:
            oHour = 24 + oHour
    answerHour=str(oHour)
    answerMin=str(oMin)
    if (len(answerMin)<2 and answerHour !='0'):
        answerMin='0'+answerMin
    if answerHour=='0':
        answerHour=''
    answer = answerHour + answerMin
    return answer


inp = list(input())

print(makeTime(inp, True, 0, 0)+" in Ottawa")
print(makeTime(inp, False, 3, 0)+" in Victoria")
print(makeTime(inp, False, 2, 0)+" in Edmonton")
print(makeTime(inp, False, 1, 0)+" in Winnipeg")
print(makeTime(inp, True, 0, 0)+" in Toronto")
print(makeTime(inp, True, 1, 0)+" in Halifax")
print(makeTime(inp, True, 1, 30)+" in St. John's")


