def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"mid : {mid}")
        print(f"left : {left}")
        print(f"right : {right}")
        if data[mid] == value:
            # 중앙 값과 찾는 값이 일치하면 리턴
            return mid
        elif data[mid] < value:
            # 중앙값보다 찾는 값이 크면 검색 범위의 왼쪽을 바꿈
            left = mid + 1
        else:
            # 중앙값보다 찾는 값이 작으면 검색 범위의 오른쪽을 바꿈
            right = mid - 1
        print('-'*20)
    return -1

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 90))
