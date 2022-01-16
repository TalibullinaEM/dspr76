import numpy as np
def random_predict(number: int = 1):
    count = 0
    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток угадывается число, при 1000 подходов

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) #  Закрепили сид
    random_array = np.random.randint(1, 101, size = (1000)) #   создали массив из 1000 целых чисел от 1 до 100 на кот.проверяется алгоритм 
    for number in random_array :
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))     #  посчитали среднее этого списка
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)
    