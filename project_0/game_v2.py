import numpy as np
#Игра в угодай число, где число будет угадывать сам ПК
def rand_pred (number: int=1) -> int: #Создаем функцию
    
    count = 0 # счетчик количества попыток
    pred_num = np.random.randint(1,101) # генерация случайного числа
    min_left = 1 # левая граница поиска
    max_right = 101 # правая граница поиска
    
    while pred_num != number: # Цикл будет воспроизводиться пока число компьютера не равно загадоному
        
        count += 1
        if pred_num < number: # Угадываем число если оно меньше
            min_left = pred_num # Смещаем левую границу
            pred_num = ((min_left + max_right) // 2) # следующие значение числа будет равно средней сумме левой и правое граници
            
        elif pred_num > number: # Угадываем число если оно больше
            max_right = pred_num # Смещаем правую границу
            pred_num = ((min_left + max_right) // 2) # следующие значение числа будет равно средней сумме левой и правое граници  
            
    return count

def score_game(random_predict) -> int:
    
    count_ls = [] # список для сохранения попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # случайный список чисел 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # среднее количество попыток

    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    ##RUN
    score_game(rand_pred)