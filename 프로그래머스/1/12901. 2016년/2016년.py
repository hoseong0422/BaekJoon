month = {
    "1" : 31,
    "2" : 29,
    "3" : 31,
    "4" : 30,
    "5" : 31,
    "6" : 30,
    "7" : 31,
    "8" : 31,
    "9" : 30,
    "10" : 31,
    "11" : 30,
    "12" : 31
}

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

def solution(a, b):
    total_days = 0
    for mon in range(1, int(a)):
        total_days += month[str(mon)]
    answer = days[(total_days + 4 + int(b)) % 7]
    return answer