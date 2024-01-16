y, m, d = map(str, input().split('-'))
if int(m) == 1:
    if int(d) >= 20:
        print('Aquarius')
    else:
        print('Capricorn')
elif int(m) == 2:
    if int(d) >= 19:
        print('Pisces')
    else:
        print('Aquarius')
elif int(m) == 3:
    if int(d) >= 21:
        print('Aries')
    else:
        print('Pisces')
elif int(m) == 4:
    if int(d) >= 20:
        print('Taurus')
    else:
        print('Aries')
elif int(m) == 5:
    if int(d) >= 21:
        print('Gemini')
    else:
        print('Taurus')
elif int(m) == 6:
    if int(d) >= 21:
        print('Cancer')
    else:
        print('Gemini')
elif int(m) == 7:
    if int(d) >= 23:
        print('Leo')
    else:
        print('Cancer')
elif int(m) == 8:
    if int(d) >= 23:
        print('Virgo')
    else:
        print('Leo')
elif int(m) == 9:
    if int(d) >= 23:
        print('Libra')
    else:
        print('Virgo')
elif int(m) == 10:
    if int(d) >= 23:
        print('Scorpio')
    else:
        print('Libra')
elif int(m) == 11:
    if int(d) >= 23:
        print('Sagittarius')
    else:
        print('Scorpio')
elif int(m) == 12:
    if int(d) >= 22:
        print('Capricorn')
    else:
        print('Sagittarius')
