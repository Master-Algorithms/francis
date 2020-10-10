def solution(food_times, k):
    answer = 0
    length = len(food_times)
    
    for _ in range(k):
        food_times[answer] -= 1
        answer += 1
        
        if answer >= length:
            answer = 0
        
        while food_times[answer] == 0:
            answer += 1
            if answer >= length:
                answer = 0
        
    answer += 1
    
    return answer
