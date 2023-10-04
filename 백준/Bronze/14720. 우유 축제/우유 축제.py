N = int(input())
milk_shops = list(map(int, input().split()))
milks = []

for milk_shop in milk_shops:
    if milk_shop == 0 and len(milks) == 0:
        milks.append(milk_shop)
    elif milk_shop == 0 and milks[-1] == 2:
        milks.append(milk_shop)
    elif milk_shop == 1:
        if len(milks) != 0 and milks[-1] == 0:
            milks.append(milk_shop)
    elif milk_shop == 2:
        if len(milks) != 0 and milks[-1] == 1:
            milks.append(milk_shop)
print(len(milks))