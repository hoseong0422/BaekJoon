import sys
input = sys.stdin.readline

dic = {}

N = int(input().rstrip())
arr = tuple(map(int,input().rstrip().split()))
M = int(input().rstrip())
arr2= tuple(map(int,input().rstrip().split()))

for i in range(len(arr2)):
    dic[arr2[i]] = 0

for idx in range(len(arr)):
    if arr[idx] in dic.keys():
        dic[arr[idx]] += 1

print(*dic.values())