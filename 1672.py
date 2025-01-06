dnaMap={"AA":"A",
     "GA":"C",
     "CA":"A",
     "TA":"G",

     "AG":"C",
     "GG":"G",
     "CG":"T",
     "TG":"A",

     "AC":"A",
     "GC":"T",
     "CC":"C",
     "TC":"G",

     "AT":"G",
     "GT":"A",
     "CT":"G",
     "TT":"T",
     }

leng = input()
prob = input()
prob_list = list(prob)
answer = ""

while(len(prob_list)>1):
    chk = prob_list[-1]+prob_list[-2]
    chk = dnaMap[chk]
    prob_list.pop(len(prob_list)-1)
    prob_list.pop(len(prob_list)-1)
    prob_list.append(chk)

for i in prob_list:
    answer+=i
    
print(answer)
