import numpy as np


def euler_to_rotation_matrix(angles):
    rad = np.radians(angles)
    rad_x, rad_y, rad_z = rad

    R_x = np.array([[1, 0, 0],
                    [0, np.cos(rad_x), np.sin(rad_x)],
                    [0, -np.sin(rad_x), np.cos(rad_x)]])

    R_y = np.array([[np.cos(rad_y), 0, -np.sin(rad_y)],
                    [0, 1, 0],
                    [np.sin(rad_y), 0, np.cos(rad_y)]])

    R_z = np.array([[np.cos(rad_z), np.sin(rad_z), 0],
                    [-np.sin(rad_z), np.cos(rad_z), 0],
                    [0, 0, 1]])

    R = R_z @ R_y @ R_x
    return R


angles = [25.399051233106778, -54.101700051821325, 5.637043873925570]
rotation_matrix = euler_to_rotation_matrix(angles)
print(rotation_matrix)
