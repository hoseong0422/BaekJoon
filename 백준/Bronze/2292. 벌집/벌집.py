n = int(input())

# 최초 벌집 개수
nums = 1
cnt = 1

# 입력값이 벌집의 갯수보다 클때까지 반복
while n > nums:
    # 벌집은 6의 배수로 증가한다.
    nums += 6 * cnt
    cnt += 1
print(cnt)