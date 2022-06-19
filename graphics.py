import math
import matplotlib.pyplot as plt
import numpy as np
# y = - (g/2v0^2) * x^2 + y0
# a = - (g/2v0^2)
# c = y0


def print_graphic(orig_coord, coord, coord_bomb):
    """
    Функция для построения графика падения бомбы

    :param orig_coord: значения для построения графика фактической траектории подения АБ
    :param coord: значения для построения графика вычисленной траектории подения АБ
    """
    x = []
    for i in coord_bomb:
        if i[0] * i[2] < 1:
            x.append(i[0] + i[2])
        else:
            x.append(math.sqrt(i[0] ** 2 + i[2] ** 2))
    x = np.array(x)
    y = []
    for i in coord_bomb:
        y.append(i[1])
    y = np.array(y)
    x1 = np.arange(coord[4], coord[0], 20)
    y1 = (coord[1] * x1 ** 2) + (coord[2] * x1) + coord[3]
    plt.xlabel('Расстояние м.', color='gray')
    plt.ylabel('Высота м.', color='gray')
    plt.plot(x, y, 'b*', orig_coord[0], 0, 'b+', x1, y1, 'g', coord[0], 0, 'r.')
    plt.legend(['Точки использованные для апроксимации', 'Фактическя точка падения АБ', 'Вычисленная траектория',
                'Вычисленная точка падения АБ'], loc=3)
    plt.show()
