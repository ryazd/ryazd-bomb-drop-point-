import math
import copy


def inverse_transition_matrix(coord_bomb, x, z, angle):
    """
    Функция для перехода из новой СК в старую
    :param coord_bomb: коопдинаты
    :param x: смещение СК
    :param z: смещение СК
    :param angle: угол на который была повенута СК
    :return: координаты
    """
    for coord in coord_bomb:
        if angle != 0:
            new_x = (math.cos(angle) * coord[0]) + (math.cos(math.radians(90) + angle) * coord[2])
            new_z = (math.cos(math.radians(90) - angle) * coord[0]) + (math.cos(angle) * coord[2])
            coord[0] = new_x
            coord[2] = new_z
        coord[0] += x
        coord[2] += z
    return coord_bomb


def angle_alpha(old_vti):
    """
    Функция для расчета угла поворота новой СК относительно начальной

    :param old_vti: координаты ВТИ в начальной системе координат
    :return: угол на которой необходимо повернуть СК
    """
    x = abs(abs(old_vti[1][0]) - abs(old_vti[0][0]))
    z = abs(abs(old_vti[1][2]) - abs(old_vti[0][2]))

    c = math.sqrt(x ** 2 + z ** 2)
    angle = math.degrees(math.asin(x / c))
    if old_vti[1][2] == old_vti[0][2]:
        if old_vti[1][0] > old_vti[0][0]:
            angle = 0
        else:
            angle += 360 - 90
    elif old_vti[1][0] == old_vti[0][0]:
        if old_vti[1][2] > old_vti[0][2]:
            angle += 90 * 3
        else:
            angle += 90
    elif old_vti[1][0] > old_vti[0][0]:
        if old_vti[1][2] < old_vti[0][2]:
            angle -= 90
    elif old_vti[1][2] > old_vti[0][2]:
        angle = 360 - angle
    else:
        angle += 180
    return angle


def transition_matrix(mas, x, z, angle):
    """
    Функция для расчета координат ВТИ в новой СК

    :param mas: координаты ВТИ
    :param x: координата на которую смещается СК
    :param z: координата на которую смещается СК
    :param angle: угол поворотв СК
    """
    mas[0] -= x
    mas[2] -= z
    if angle != 0:
        new_x = (math.cos(angle) * mas[0]) + (math.cos(math.radians(90) - angle) * mas[2])
        new_z = (math.cos(math.radians(90) + angle) * mas[0]) + (math.cos(angle) * mas[2])
        mas[0] = new_x
        mas[2] = new_z


def coord_of_bomb(vti, dist):
    """
    Функция для расчета координат АБ с помощью дальности до ВТИ

    :param vti: координаты ВТИ
    :param dist: расстояние между АБ и ВТИ
    :return:
    """
    x = (vti[1][0] ** 2 + dist[0] ** 2 - dist[1] ** 2) / (2 * vti[1][0])
    z = (vti[2][0] ** 2 + vti[2][2] ** 2 + dist[0] ** 2 - dist[2] ** 2 - (2 * vti[2][0] * x)) / (2 * vti[2][2])
    y = math.sqrt(dist[0] ** 2 - x ** 2 - z ** 2)
    coord = [x, y, z]
    return coord


def reverce_coord(mas, angle_alpha, x, z):
    """
    Функция для перехода из новой СК в начальную

    :param mas: координаты АБ
    :param angle_alpha: угол на который была повернута СК
    :param x: смещение оси относительно исходной СК
    :param z: смещение оси относительно исходной СК
    :return: координаты в исходной СК
    """
    if angle_alpha != 0:
        angle = math.radians(360 - angle_alpha)
    else:
        angle = math.radians(0)
    new_x = (math.cos(angle) * mas[0]) + (math.cos(math.radians(90) - angle) * mas[2])
    new_z = (math.cos(math.radians(90) + angle) * mas[0]) + (math.cos(angle) * mas[2])
    mas[0] = x + new_x
    mas[2] = z + new_z
    return mas


def init_new_coord_vti(old_vti):
    """
    Функция для иннициализации массива координат ВТИ в новой СК

    :param old_vti: координат в ВТИ в начальной СК
    :return: массив координат ВТИ в новой СК и угол поворота новой СК относительно начальной
    """
    new_vti = copy.deepcopy(old_vti)
    new_vti[0][0] = new_vti[0][2] = 0
    angle_a = angle_alpha(old_vti)
    transition_matrix(new_vti[1], old_vti[0][0], old_vti[0][2], math.radians(angle_a))
    transition_matrix(new_vti[2], old_vti[0][0], old_vti[0][2], math.radians(angle_a))
    return new_vti, angle_a
