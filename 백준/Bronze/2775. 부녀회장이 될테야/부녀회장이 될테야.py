# 배열 이용해서 풀어보기
case = int(input())

for _ in range(case):
    # 층
    k = int(input()) 
    # 호수
    n = int(input())
    base = [ _ for _ in range(1, n+1)]
    
    for i in range(k):
        for j in range(1, n):
            base[j] += base[j-1]
    print(base[-1])