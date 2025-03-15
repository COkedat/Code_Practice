"""문제
단어 사다리란 퍼즐의 한 종류인데, 두 단어가 주어지면 한 단어에서 한 글자씩 바꿔서 다른 단어를 만드는 것이다. 이 게임은 좋은 어휘력과 맞춤법이 필요하다. 그래서 정답인지 아닌지 확인하는 게 너무 지루하고 귀찮다. 

한 쌍의 단어가 단어 사다리가 되는 조건은 다음과 같다:

단어의 길이가 같고
반드시 한 글자씩 바뀌어야한다.
단어 사다리가 가능한 지 판별하는 프로그램을 작성하시오.

입력
입력이 여러 번 주어지는데, #이 입력되기 전까지를 하나의 테스트케이스로 간주한다.

각 테스트케이스는 3자 이상 20자 이하의 대문자 알파벳으로 된 단어들이 순서대로 입력된다. 입력의 마지막 줄에는 #이 주어진다.

출력
단어 사다리가 가능하다면 'Correct'를, 아니면 'Incorrect'를 출력한다."""

# 대충 단어비교 함수
def able(word1, word2):
    # 길이가 다르면 False
    if len(word1) != len(word2):  
        return False
    
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    # 한 글자만 다를 때 True
    return diff_count == 1  

# 초기화
answer = []
words = []
# 반복문
while True:
    word = input()

    # #일경우
    if word == "#":
        # 입력된 단어가 있을 경우만 검사
        if words:  
            #총합 검사
            is_correct = all(able(words[i], words[i + 1]) for i in range(len(words) - 1))
            answer.append("Correct" if is_correct else "Incorrect")
            words = []  # 새로운 테스트 케이스를 위해 초기화
        # 더 이상 입력이 없으면 종료
        else:
            break  
    # #이 아닐경우 추가
    else:
        words.append(word)

# 출력
for ans in answer:
    print(ans)



