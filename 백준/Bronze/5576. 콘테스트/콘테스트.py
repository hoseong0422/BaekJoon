w_points = [int(input()) for _ in range(10)]
k_points = [int(input()) for _ in range(10)]

w_points.sort()
k_points.sort()

print(sum(w_points[-3:]), sum(k_points[-3:]), sep=' ')