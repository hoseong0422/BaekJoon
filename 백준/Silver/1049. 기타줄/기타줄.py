N, M = map(int, input().split())

single_list = []
package_list = []
for _ in range(M):
    p, s = map(int, input().split())
    single_list.append(s)
    package_list.append(p)

min_s = min(single_list)
min_p = min(package_list)

if min_p < min_s * 6:
    if min_p < (N % 6) * min_s:
        print((N // 6) * min_p + min_p)
    else:
        print((N // 6) * min_p + (N % 6) * min_s)

elif min_p >= min_s * 6:
    print(N * min_s)