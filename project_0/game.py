import numpy as np

number = np.random.randint(1,101)
count = 0

while True:
    count += 1
    pred_num = int(input('Угадайте число от 1 до 100\n'))
    if pred_num > number:
        print('Это число меньше')
    elif pred_num < number:
        print('Это число больше')
    else:
        print(f'Поздравляем, вы угодали число {number} за {count} попыток')
        break

print("hello world")