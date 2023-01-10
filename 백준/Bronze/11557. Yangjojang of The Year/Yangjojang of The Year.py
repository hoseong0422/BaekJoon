T = int(input())
for _ in range(T):
    max_alcohol = 0
    max_school = ""
    N = int(input())
    for _ in range(N):
        school, alcohol = map(str, input().split())
        
        if int(alcohol) > max_alcohol:
            max_school = school
            max_alcohol = int(alcohol)
    
    print(max_school)