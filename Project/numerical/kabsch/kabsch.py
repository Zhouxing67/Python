import csv
import numpy as np
import matplotlib.pyplot as plt


def kabsch1(P, Q):
    # 计算P， Q的质心
    centroid_P = np.mean(P, axis=0)
    centroid_Q = np.mean(Q, axis=0)
    # 均值归一到0
    P_centered = P - centroid_P
    Q_centered = Q - centroid_Q
    # 计算协方差矩阵
    H = P_centered.T.dot(Q_centered)
    # 对H做SVD分解
    U, S, VT = np.linalg.svd(H)  # SVD
    R = U.dot(VT).T
    # 这里变换为右手系
    if np.linalg.det(R) < 0:
        VT[2, :] *= -1
        R = U.dot(VT).T
    t = centroid_Q - R.dot(centroid_P)
    return R, t


def plot_3d_points(pointsA, pointsB, pointsC):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # 绘制三维点集
    ax.scatter(pointsA[:, 0], pointsA[:, 1], pointsA[:, 2], s=20, c="b",
               marker="o")
    ax.scatter(pointsB[:, 0], pointsB[:, 1], pointsB[:, 2], s=20, c="k",
               marker="o")
    ax.scatter(pointsC[:, 0], pointsC[:, 1], pointsC[:, 2], s=20, c="r",
               marker="o")
    # 设置坐标轴标签
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # 显示图像
    plt.show()


def read_data(filename):
    with open(filename, newline="") as csvfile:
        # 创建 CSV 文件读取器
        reader = csv.reader(csvfile)
        points = []
        # 逐行读取文件内容
        for row in reader:
            # 在这里进行处理，row 是一个列表，包含每一行的数据
            # 假设每行数据为 x, y, z
            x, y, z = map(float, row)
            points.append([x, y, z])
    return np.array(points)
