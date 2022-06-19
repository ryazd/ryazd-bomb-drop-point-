import math

"""

Модуль для вычисления расстояния между ВТИ и АБ в каждый момент времени

"""

G = 9.81    # метр/секунда


def coord_bomb_in_moment(t_moment, v_0, bomb_start_coord, heading_angle):
    """
    Функция определяющая координаты бомбы в момент времени t_moment

    :param bomb_start_coord: начальные координаты АБ
    :param t_moment: время с начала падения АБ
    :param v_0: горизонтальная скорость АБ
    :param heading_angle: угол курса
    :return координаты АБ в момент времени t
    """
    bomb_coord = [0, 0, 0]
    x = v_0 * t_moment
    bomb_coord[1] = bomb_start_coord[1] - (G * x ** 2 / (2 * v_0 ** 2))
    angle = math.radians(heading_angle)
    bomb_coord[0] = x * math.cos(angle) + bomb_start_coord[0]
    bomb_coord[2] = x * math.sin(angle) + bomb_start_coord[2]
    return bomb_coord


def coord_bomb_drop(bomb_start_coord, v_0, heading_angle):
    """
    Функция для вычисления времени и координат падения АБ

    :param bomb_start_coord: массив с начальными координатами АБ
    :param v_0: горизонтальная скорость АБ
    :param heading_angle: угол курса
    :return x_1, z_1, t: координаты падения бомбы и время падения
    """
    x = math.sqrt(bomb_start_coord[1] * 2 * v_0 * v_0 / G)
    angle = math.radians(heading_angle)
    z_1 = x * math.sin(angle) + bomb_start_coord[2]
    x_1 = x * math.cos(angle) + bomb_start_coord[0]
    t = x / v_0                                             # время падения
    return x_1, z_1, t


def len_of_vector(a, b):
    """
    Функция для вычисления длины вектора

    :param a: вектор
    :param b: вектор
    :return: длина вектора
    """
    len_vec = 0

    for i in range(3):
        len_vec += (a[i] - b[i]) ** 2
    return math.sqrt(len_vec)


def dist_to_vti(bomb_coord, vti):
    """
    Функция для вычисления расстояния до АБ

    :param bomb_coord: координаты бомбы
    :param vti: массив координат ВТИ
    :return массив для записи расстояний
    """
    dist = [0, 0, 0]
    for i in range(3):
        dist[i] = len_of_vector(bomb_coord, vti[i])
    return dist


def dist_to_ab_inmoment(bomb_start_coord, v_0, heading_angle, vti, time):
    """
    Функция для вычисления растояния до АБ в в момент времени time

    :param bomb_start_coord: началные координат АБ
    :param v_0: горизонтальна скорость АБ
    :param heading_angle: угол курса
    :param vti: координаты ВТИ
    :param time: время с момента сброса
    :return: расстояние между ВТИ и АБ
    """
    bomb_coord = coord_bomb_in_moment(time, v_0, bomb_start_coord, heading_angle)
    dist = dist_to_vti(bomb_coord, vti)
    return dist
