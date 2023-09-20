N = int(input())
book_dict = {}
for _ in range(N):
    book = input()
    if book in book_dict.keys():
        book_dict[book] = book_dict[book] + 1
    else:
        book_dict[book] = 1

temp = sorted(book_dict.items(), key=lambda x:x[1], reverse=True)
answer = []
for t in temp:
    if t[1] == temp[0][1]:
        answer.append(t[0])

if len(answer) == 1:
    print(answer[0])
else:
    answer.sort()
    print(answer[0])