data = list(map(int, input().split()))

sum_data = []
for i in data:
    sum_data.append(i ** 2)
print(sum(sum_data) % 10)