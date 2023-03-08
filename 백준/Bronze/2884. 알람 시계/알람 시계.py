H, M = map(int, input().split(" "))
if H == 0:
    if M < 45:
        H = 24
        H -= 1
        M = M + 60 - 45
        print(f"{H} {M}")
    elif M >= 45:
        H = 0
        M = M - 45
        print(f"{H} {M}")
else:
    if M < 45:
        H -= 1
        M = M + 60 - 45
        print(f"{H} {M}")
    else:
        M = M - 45
        print(f"{H} {M}")