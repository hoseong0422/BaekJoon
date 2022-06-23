numbers = set(range(1, 10001))
remove_num = set() # 삭제하기 위한 숫자 set

for i in numbers:
    for j in str(i):
        i += int(j) # 생성자가 있는 숫자
    remove_num.add(i) # add: set에 요소를 추가

self_num = (numbers - remove_num)
for i in sorted(self_num):
    print(i)