n = int(input())
m = int(input())

n_lst = [input() for _ in range(n)]
m_lst = [input() for _ in range(m)]

for n_word in n_lst:
    for m_word in m_lst:
        print(f"{n_word} as {m_word}")