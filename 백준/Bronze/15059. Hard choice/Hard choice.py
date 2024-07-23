foods = list(map(int, input().split()))
passengers_choice = list(map(int, input().split()))
answer = 0

for i in range(len(foods)):
    if foods[i] < passengers_choice[i]:
        answer += passengers_choice[i] - foods[i]

print(answer)