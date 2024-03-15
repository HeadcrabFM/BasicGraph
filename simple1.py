import matplotlib.pyplot as plt
import launcher
from colorama import Fore, Back, Style

def Simple1():
    print(Fore.GREEN + 'Привет! Это моя первая простая программа с графиком)))')
    print(Style.RESET_ALL)  # Сброс цвета

    # Настройка цвета фона окна
    plt.figure(facecolor='lightblue')
    # входные значения
    x = [i * 0.1 for i in range(-100, 101)]

    # Функция, преобразующая входные значения
    y = [pow(i,3) for i in x]

    # Создание пустого графика
    plt.plot([], [])

    # Добавление горизонтальной линии для оси x
    plt.axhline(0, color='gray')

    # Добавление вертикальной линии для оси y
    plt.axvline(0, color='gray')

    # Настройка осей и заголовка
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')

    # Настройка диапазона оси x и y
    plt.xlim(left=min(x)-1, right=max(x)+1)
    plt.ylim(bottom=-1000, top=1000)

    # Отображение графика без точек
    plt.show(block=False)

    # Постепенное добавление точек на график
    for i in range(len(x)):
        plt.plot(x[i], y[i], marker='o', color=(0.255,0.0,0.220), markersize=2)  # Добавление очередной точки
        plt.pause(0.0001)  # Пауза для задержки между добавлением точек
        print(f'Добавлена точка {i}, значение: {round(y[i],6)}')

    plt.show()  # Отображение окончательного графика
    launcher.mainmenu()
