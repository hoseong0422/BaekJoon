secs = [int(input()) for i in range(4)]
total = sum(secs)

m = total // 60
s = total % 60

print(m, s, sep='\n')