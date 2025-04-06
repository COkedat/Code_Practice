def chkPalindrome(N):
    N = str(N)
    # 한자리수인경우 그냥 True
    if(len(N) == 1):
        return True
    # 길이 짝수
    if(len(N)%2 == 0):
        p1 = N[:len(N)//2]
        p2 = ''.join(reversed(N[len(N)//2:]))
        if(p1 == p2):
            return True
    # 길이 홀수
    else:
        p1 = N[:int(len(N)/2)]
        p2 = ''.join(reversed(N[int(len(N)/2)+1:]))
        if(p1 == p2):
            return True
    return False