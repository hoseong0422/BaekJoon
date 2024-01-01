m = ['a', 'i', 'y', 'e', 'o', 'u']
j = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

len_m = len(m)
len_j = len(j)

while True:
    try:
        data = input()
        answer = ''

        for d in data:
            if d.lower() in m:
                if d in m: # 소문자일경우
                    if m.index(d) + 3 >= len_m - 1:
                        answer += m[(m.index(d) + 3) % len_m]
                    else:
                        answer += m[m.index(d) + 3]
                else:
                    if m.index(d.lower()) + 3 >= len_m - 1:
                        answer += m[(m.index(d.lower()) + 3) % len_m].upper()
                    else:
                        answer += m[m.index(d.lower()) + 3].upper()
            elif d.lower() in j:
                if d in j: # 소문자일 경우
                    if j.index(d.lower()) + 10 >= len_j - 1:
                            answer += j[(j.index(d) + 10) % len_j]
                    else:
                        j.index(d)
                        answer += j[j.index(d) + 10]
                else:
                    if j.index(d.lower()) + 10 >= len_j - 1:
                            answer += j[(j.index(d.lower()) + 10) % len_j].upper()
                    else:
                        j.index(d.lower())
                        answer += j[j.index(d.lower()) + 10].upper()
            else:
                answer += d

        print(answer)
    except:
        break