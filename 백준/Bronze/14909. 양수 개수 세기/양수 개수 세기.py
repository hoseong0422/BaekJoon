data = list(map(int, input().split()))
answer = [i for i in data if i > 0]
print(len(answer))