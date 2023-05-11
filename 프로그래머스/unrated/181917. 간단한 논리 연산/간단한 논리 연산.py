def solution(x1, x2, x3, x4):
    if x1 == True or x2 == True:
        a = True
    elif x1 == False and x2 == False:
        a = False
    if x3 == True or x4 == True:
        b = True
    elif x3 == False and x4 == False:
        b = False
    if a == True and b == True:
        return True
    else:
        return False