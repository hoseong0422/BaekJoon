def sangsoo_answer():
# 입력받고
    data = list(map(str, input().split(" ")))
# [::-1] 순서 변경
    A = data[0][::-1]
    B = data[1][::-1]
# 정수형 변환
    A = int(A)
    B = int(B)

    if A > B:
        print(A)
    else:
        print(B)
sangsoo_answer()