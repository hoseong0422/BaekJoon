import re

def solution(new_id):
    # 1) 소문자로
    new_id = new_id.lower()
    
    # 2) 허용 문자만 남기기: a-z, 0-9, -, _, .
    new_id = re.sub(r"[^a-z0-9\-_.]", "", new_id)
    
    # 3) 연속된 . -> 단일 .
    new_id = re.sub(r"\.+", ".", new_id)
    
    # 4) 처음/끝의 . 제거
    new_id = new_id.strip(".")
    
    # 5) 빈 문자열이면 "a"
    if not new_id:
        new_id = "a"
        
    # 6) 15자 자르고, 끝에 . 있으면 제거
    new_id = new_id[:15].rstrip(".")

    # 7) 길이 2 이하이면 마지막 문자 반복해서 길이 3 만들기
    while len(new_id) < 3:
        new_id += new_id[-1]        
        
    return new_id