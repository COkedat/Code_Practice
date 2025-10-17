N = int(input())
for _ in range(N):
    A, B = map(int,input().split(" "))
    result = [0,0]
    if A != 0:
        if A <= 1:
            result[0] = 5000000
        elif A <= 3:
            result[0] = 3000000
        elif A <= 6:
            result[0] = 2000000
        elif A <= 10:
            result[0] = 500000
        elif A <= 15:
            result[0] = 300000
        elif A <= 21:
            result[0] = 100000
    if B != 0:
        if B <= 1:
            result[1] = 5120000
        elif B <= 3:
            result[1] = 2560000
        elif B <= 7:
            result[1] = 1280000
        elif B <= 15:
            result[1] = 640000
        elif B <= 31:
            result[1] = 320000
    print(sum(result))
            
          