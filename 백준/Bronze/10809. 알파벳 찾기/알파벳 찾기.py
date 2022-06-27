import string
# 소문자 리스트
lower_alpha = list(string.ascii_lowercase)
#-1이 들어가있는 리스트 만들기
find_locate = [-1 for _ in range(len(lower_alpha))]
# 단어 입력받기
word = str(input())

# 단어의 길이만큼 for문 돌리기
# 여기에서 i가 단어의 위치에 사용됨
for i in range(len(word)):
    # 알파벳 소문자 길이만큼 for문 돌리기
    for j in range(len(lower_alpha)):
        if word[i] == lower_alpha[j]:
            if find_locate[j] == -1:
                find_locate[j] = i

for _ in find_locate:
    print(_, end=" ")