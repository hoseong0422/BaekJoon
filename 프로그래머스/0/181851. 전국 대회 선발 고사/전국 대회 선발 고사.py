def solution(rank, attendance):
    attendee = [rank[i] for i in range(len(rank)) if attendance[i] != False]

    answer = 0
    attendee.sort()

    for i in range(3):
        if i == 0:
            answer += rank.index(attendee[i]) * 10000
        elif i == 1:
            answer += rank.index(attendee[i]) * 100
        else:
            answer += rank.index(attendee[i])
    return answer