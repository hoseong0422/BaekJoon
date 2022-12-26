x, y, w, h = map(int, input().split())

if x > w:
    if x - w <= x:
        x_len = int(x - w)
    else:
        x_len = x
        
else:
    if w - x <= x:
        x_len = int(w - x)
    else:
        x_len = x

if y > h:
    if y - h <= y:
        y_len = int(y - h)
    else:
        y_len = y
else:
    if h - y <= y:
        y_len = int(h - y)
    else:
        y_len = y
    
if x_len < y_len:
    print(x_len)
else:
    print(y_len)