N = int(input())

cheese_list = []

cheeses = list(map(str, input().split()))

for cheese in cheeses:
    if cheese[-6:] == 'Cheese':
        cheese_list.append(cheese)

if len(set(cheese_list)) >= 4:
    print('yummy')
else:
    print('sad')