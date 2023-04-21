limit = int(input())
speed = int(input())
diff = speed - limit
if diff > 0:
    if diff <= 20:
        print('You are speeding and your fine is $100.')
    elif diff <= 30:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $500.')
else:
    print('Congratulations, you are within the speed limit!')