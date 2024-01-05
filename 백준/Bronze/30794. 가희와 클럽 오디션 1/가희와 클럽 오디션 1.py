scores = {
    'miss' : 0,
    'bad' : 200,
    'cool' : 400,
    'great' : 600,
    'perfect' : 1000
}

lv, score = map(str, input().split())

print(int(lv) * scores[score])