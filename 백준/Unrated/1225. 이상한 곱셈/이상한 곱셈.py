A, B = map(str, input().split())
a_list = [int(i) for i in A]
answer = 0
for b in B:
    answer += sum(a_list) * int(b)
print(answer)