try:
    while True :
        data = input()
        word_dict = {"e": "i", "i": "e", "E": "I", "I": "E"}
        answer = ''
        for i in range(len(data)):
            if data[i] in word_dict:
                answer += word_dict[data[i]]
            else:
                answer += data[i]
        print(answer)

except EOFError:
    exit()