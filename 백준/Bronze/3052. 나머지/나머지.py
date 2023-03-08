A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
G = int(input())
H = int(input())
I = int(input())
J = int(input())

ary = [A, B, C, D, E, F, G, H, I, J]
remains = []
for n in ary:
    r = n % 42
    remains.append(r)
print(len(set(remains)))