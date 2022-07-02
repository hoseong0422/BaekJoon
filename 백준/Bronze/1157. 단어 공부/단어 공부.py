# 입력받아 소문자로 변환
data = input().lower()
# 중복 제거된 알파뱃 리스트 생성
alpha_list = list(set(data))
cnt = []

for alpha in alpha_list:
    # alpha_list의 요소들이 각각 data안에 몇개씩 있는지?
    count = data.count(alpha)
    cnt.append(count)

# cnt 리스트에 max(cnt):가장 큰 값을 갖는 요소가 몇개인지?
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    # alpha_list로 for문을 돌렸기때문에 alpha_list의 알파벳 등장 빈도가 
    # cnt리스트에 alpha_list와 동일한 인덱스로 저장되어 있다.
    # cnt.index(max(cnt)) : max(cnt)의 인덱스
    print(alpha_list[cnt.index(max(cnt))].upper())