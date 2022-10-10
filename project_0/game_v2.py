import numpy as np
#Игра в угодай число, где число будет угадывать сам ПК
def rand_pred (number: int=1) -> int: #Создаем функцию
    
    count = 0
    pred_num = np.random.randint(1,101)
    min_left = 1
    max_right = 101
    
    while pred_num != number:
        
        count += 1
        if pred_num < number:
            min_left = pred_num
            pred_num = ((min_left + max_right) // 2)
            
        elif pred_num > number:
            max_right = pred_num
            pred_num = ((min_left + max_right) // 2)   
            
    return count

def score_game(random_predict) -> int:
    
    count_ls = [] # список для сохранения попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # случайный список чисел 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # реднее количество попыток

    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    
    score_game(rand_pred)