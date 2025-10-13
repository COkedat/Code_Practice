nums = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve"}
min10 = {1:"ten",2:"twenty",3:"thirty",4:"fourty",5:"fifty"}
min10to20 = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
H=input()
M=input()
H=int(H)
if(M=="00" or M=="0"):
    print(f"{nums[H]} o' clock")
else:
    M_num = int(M)
    M = list(M)
    if(M_num < 10):
        M10=0
        M1=int(M[0])
    else:
        M10=int(M[0])
        M1=int(M[1])
    H_plus = H+1 if H+1 < 13 else 1
    if M_num == 15:
        print(f"quarter past {nums[H]}")
    elif M_num == 30:
        print(f"half past {nums[H]}")
    elif M_num == 45:
        print(f"quarter to {nums[H_plus]}")
    elif M_num == 1:
        print(f"{nums[M1]} minute past {nums[H]}")
    elif M_num < 10:
        print(f"{nums[M1]} minutes past {nums[H]}")
    elif M_num < 20:
        print(f"{min10to20[M_num]} minutes past {nums[H]}")
    elif M_num < 30:
        if M1 !=0:
            print(f"{min10[M10]} {nums[M1]} minutes past {nums[H]}")
        else:
            print(f"{min10[M10]} minutes past {nums[H]}")
    else:
        M_num=60-M_num
        M10=M_num//10
        M1=M_num%10
        if M_num == 1:
            print(f"{nums[M1]} minute to {nums[H_plus]}")
        elif M_num < 10:
            print(f"{nums[M1]} minutes to {nums[H_plus]}")
        elif M_num < 20:
            print(f"{min10to20[M_num]} minutes to {nums[H_plus]}")
        elif M_num < 30:
            if M1 !=0:
                print(f"{min10[M10]} {nums[M1]} minutes to {nums[H_plus]}")
            else:
                print(f"{min10[M10]} minutes to {nums[H_plus]}")