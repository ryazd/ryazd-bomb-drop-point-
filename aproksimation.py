import math
import numpy


def init_sum(matrix, num_of_coord):
    """
    Массив для суммы коэффицинтов
    :param matrix: матрица коэффициентов
    :param num_of_coord: количество координат
    :return: массив сумм коэф.
    """
    mas = [0, 0, 0, 0, 0, 0, 0]
    for i in range(7):
        sum = 0
        for j in range(num_of_coord):
            sum += matrix[j][i]
        mas[i] = sum
    return mas


def init_matrix(coord_ab):
    """
    Инициализация матрицы коэффициентов
    :param coord_ab:
    :return: матрица
    """
    mas = [0, 0, 0, 0, 0, 0, 0]
    mas[1] = coord_ab[1]
    mas[0] = math.sqrt(coord_ab[0] ** 2 + coord_ab[2] ** 2)
    mas[2] = mas[0] ** 2
    mas[3] = mas[0] ** 3
    mas[4] = mas[0] ** 4
    mas[5] = mas[0] * mas[1]
    mas[6] = mas[2] * mas[1]
    return mas


def solve_matrix(m_sum, num_of_coord):
    """
    Функция для решения матрицы

    :param m_sum:
    :param num_of_coord:
    :return: матрица коэффициентов уравнения
    """
    mat = numpy.array([[m_sum[4], m_sum[3], m_sum[2]], [m_sum[3], m_sum[2], m_sum[0]], [m_sum[2], m_sum[0], num_of_coord]])
    vec = numpy.array([m_sum[6], m_sum[5], m_sum[1]])
    return numpy.linalg.solve(mat, vec)


def discriminant(a, b, c):
    d = b ** 2 - (4 * a * c)
    if d == 0:
        return (b / (2 * a)) * -1
    else:
        x_1 = (math.sqrt(d) - b) / (2 * a)
        x_2 = (math.sqrt(d) * -1 - b) / (a * 2)
        return max(x_2, x_1)


def aproksimation_coord(coord_bomb):
    """
    Функция для апроксимации методом наименьших квадратов
    :param coord_bomb: координаты АБ
    :return:коэффициенты уравнения
    """
    matrix = []
    for i in range(len(coord_bomb)):
        matrix.append(init_matrix(coord_bomb[i]))
    matrix_sum = init_sum(matrix, len(coord_bomb))
    matrix_abc = solve_matrix(matrix_sum, len(coord_bomb))
    a = (matrix_abc[0])
    b = matrix_abc[1]
    c = (matrix_abc[2])
    x_0 = (b / (2 * a)) * -1
    y_0 = (a * x_0 * x_0) + (b * x_0) + c
    x_drop = discriminant(a, b, c)
    print("вычисленные значения:\n", 'точка падения:', x_drop, 'коэф. а:', a, "y_0:", y_0, "x_0:", x_0)
    return [x_drop, a, b, c, x_0]
