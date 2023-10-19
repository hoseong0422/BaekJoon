data = "WelcomeToSMUPC"
N = int(input())

if N > len(data):
    N %= len(data)

print(data[N -1])