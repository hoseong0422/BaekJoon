while True:
    name, age, weight = map(str, input().split())
    if name == '#' and age == weight == '0':
        break
    if int(age) >= 18 or int(weight) >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')