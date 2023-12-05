answer = ""
tag = False
stack = ""
for i in input():
    if i == "<":
        tag = True
        answer += stack[::-1]
        stack = ""
        answer += i
        continue
    elif i == ">":
        tag = False
        answer += i
        continue
    elif i == " ":
        answer += stack[::-1] + " "
        stack = ""
        continue
        
    if tag:
        answer += i
    else:
        stack += i
print(answer + stack[::-1])