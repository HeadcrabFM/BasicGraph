# простейший график который просто выдаёт все значения из таблички)

import pandas as pd
import matplotlib.pyplot as plt

def Weight():
    # Настройка цвета фона окна
    plt.figure(facecolor='pink')

    # Чтение данных из эксель-файла
    data = pd.read_excel('base.xlsx')
    # Извлечение значений из столбца 'x'
    y = data['weight'].tolist()

    # входные значения
    x = [i * 1 for i in range(0, len(y))]

    # Создание пустого графика
    plt.plot([], [])

    # Добавление горизонтальной линии для оси x
    plt.axhline(0, color='gray')

    # Добавление вертикальной линии для оси y
    plt.axvline(0, color='gray')

    # Настройка осей и заголовка
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График веса')

    # Настройка диапазона оси x и y
    plt.xlim(left=min(x), right=max(x) + 1)
    plt.ylim(bottom=min(y) - 1, top=max(y) + 1)



    # Постепенное добавление точек на график
    for i in range(len(x)):
        plt.plot(x[i], y[i], '-o', color='red', markersize=1)  # Добавление очередной точки
        plt.pause(0.01)  # Пауза для задержки между добавлением точек

    plt.plot(x, y, '-o', color='red', markersize=0.5)  # Добавление очередной точки
    plt.show(block=True)  # Отображение окончательного графика
