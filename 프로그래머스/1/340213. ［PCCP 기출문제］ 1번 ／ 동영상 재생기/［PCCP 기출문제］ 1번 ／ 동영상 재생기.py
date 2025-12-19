def convert_time_to_sec(t):
    
    minutes = t.split(':')[0]
    seconds = t.split(':')[-1]
    
    return int(minutes) * 60 + int(seconds)
    
def convert_sec_to_time(i):
    
    minutes = i // 60
    seconds = i % 60
    
    return f'{minutes:02d}:{seconds:02d}'

def solution(video_len, pos, op_start, op_end, commands):
    
    video_sec = convert_time_to_sec(video_len)
    pos_sec = convert_time_to_sec(pos)
    op_start_sec = convert_time_to_sec(op_start)
    op_end_sec = convert_time_to_sec(op_end)
    
    for command in commands:
        
        # 오프닝 구간 건너뛰기
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        
        if command == 'prev':
            pos_sec -= 10
        else:
            # next
            pos_sec += 10
        
        if pos_sec < 0:
            pos_sec = 0
        
        if pos_sec > video_sec:
            pos_sec = video_sec

    # 오프닝 구간 건너뛰기
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
                
    answer = convert_sec_to_time(pos_sec)
    return answer