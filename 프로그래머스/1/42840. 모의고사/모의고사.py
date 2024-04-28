def solution(answers):
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_dict = {
        "answer_a" : 0, 
        "answer_b" : 0, 
        "answer_c" : 0
        }
    
    for i in range(len(answers)):

        if i >= len(supo_1):
            if answers[i] == supo_1[i % (len(supo_1))]:
                answer_dict['answer_a'] += 1
        else:
            if supo_1[i] == answers[i]:
                answer_dict['answer_a'] += 1
        
        if i >= len(supo_2):
            if answers[i] == supo_2[i % (len(supo_2))]:
                answer_dict['answer_b'] += 1
        else:
            if supo_2[i] == answers[i]:
                answer_dict['answer_b'] += 1

        if i >= len(supo_3):
            if answers[i] == supo_3[i % (len(supo_3))]:
                answer_dict['answer_c'] += 1
        else:
            if supo_3[i] == answers[i]:
                answer_dict['answer_c'] += 1

    sorted_dict = sorted(answer_dict.items(), key = lambda x : x[1], reverse=True)

    answer = []
    for i in range(len(sorted_dict)):
        if len(answer) == 0:
            if sorted_dict[i][0] == "answer_a":
                answer.append(1)
            elif sorted_dict[i][0] == "answer_b":
                answer.append(2)
            elif sorted_dict[i][0] == "answer_c":
                answer.append(3)
        
        elif sorted_dict[i][1] == sorted_dict[i-1][1]:
            if sorted_dict[i][0] == "answer_a":
                answer.append(1)
            elif sorted_dict[i][0] == "answer_b":
                answer.append(2)
            elif sorted_dict[i][0] == "answer_c":
                answer.append(3)
        
        elif sorted_dict[i][1] != sorted_dict[i-1][1]:
            break
            
    answer.sort()
    return answer