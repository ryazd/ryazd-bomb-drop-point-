import math
from dist_to_coord import inverse_transition_matrix
from dist_to_coord import init_new_coord_vti
from dist_to_coord import coord_of_bomb
from calculation_dist import coord_bomb_drop
from calculation_dist import dist_to_ab_inmoment
from aproksimation import aproksimation_coord
from graphics import print_graphic


def graphic(bomb_start_coord, old_coord_bomb, v_0, heading_angle, g):
    coord_for_graph = aproksimation_coord(old_coord_bomb)
    x1, z1, t = coord_bomb_drop(bomb_start_coord, v_0, heading_angle)
    x_orig = math.sqrt(x1 ** 2 + z1 ** 2)
    a_orig = - (g / (2 * v_0 ** 2))
    x_0 = math.sqrt(bomb_start_coord[0] ** 2 + bomb_start_coord[2] ** 2)
    print('фактические значения:\n', 'точка падения:', x_orig, 'коэф а:', a_orig, 'y_0:', bomb_start_coord[1], 'x_0:', x_0)
    #prob.d3_grapf(old_coord_bomb)
    print_graphic([x_orig, a_orig, bomb_start_coord[1]], coord_for_graph, old_coord_bomb)


def main():
    bomb_start_coord = [0, 1000, 0]                 # начальные координаты АБ метры
    v_0 = 20                                        # воздушная скорость самолета метер/секунды
    g = 9.81                                        # метер/секунды
    heading_angle = 20                              # угол курса градусы
    vti = [[0, 0, 0], [500, 0, 0], [0, 0, 500]]     # координаты наземных измерителей

    dist = []
    for i in range(0, 4):
        dist.append(dist_to_ab_inmoment(bomb_start_coord, v_0, heading_angle, vti, i))  # запись в массив растояния до АБ
    new_vti, angle_alpha = init_new_coord_vti(vti)                            #
    coord_of_ab = []
    for i in range(len(dist)):
        coord_of_ab.append(coord_of_bomb(new_vti, dist[i]))
    old_coord_bomb = inverse_transition_matrix(coord_of_ab, vti[0][0], vti[0][2], math.radians(angle_alpha))
    graphic(bomb_start_coord, old_coord_bomb, v_0, heading_angle, g)


if __name__ == '__main__':
    main()
