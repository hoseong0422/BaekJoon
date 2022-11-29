def solution(id_pw, db):
    answer = ''
    id = id_pw[0]
    pw = id_pw[1]
    cnt = 0
    for data in db:
        if data[0] == id:
            cnt += 1
            if data[1] == pw:
                return 'login'
            elif data[1] != pw:
                return 'wrong pw'
    if cnt == 0:
        return 'fail'