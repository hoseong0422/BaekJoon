data = [input() for i in range(3)]

for i in range(len(data)):
    if data[i].isdigit():
        next = int(data[i]) + len(data) - i
        break

if next % 3 == 0:
    if next % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif next % 5 == 0:
    print('Buzz')
else:
    print(next)