X = int(input())
for i in range(X):
    data = list(map(int, input().split()))
    N = data[0]
    class_x = data[1:]
    max_x = max(class_x)
    min_x = min(class_x)
    class_x.sort(reverse=True)
    largest_gap = 0
    for j in range(len(class_x)):
        if j == len(class_x) - 1:
            continue
        else:
            temp_gap = class_x[j] - class_x[j + 1]
            if temp_gap > largest_gap:
                largest_gap = temp_gap
    print(f'Class {i+1}')
    print(f'Max {max_x}, Min {min_x}, Largest gap {largest_gap}')