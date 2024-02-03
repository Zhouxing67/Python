import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# 定义牛顿插值函数
def newton_interpolation(x, y, points):
    n = len(x)
    # 计算差商表
    coefficients = []
    differences_table = np.zeros((n, n))
    differences_table[:, 0] = y
    for j in range(1, n):
        for i in range(j, n):
            differences_table[i][j] = (
                differences_table[i][j - 1] - differences_table[i - 1][j - 1]
            ) / (x[i] - x[i - j])
    for j in range(n):
        coefficients.append(differences_table[j][j])

    # 计算估计值
    res = []
    for point in points:
        temp = [1]
        for i in range(1, n):
            temp.append(temp[i - 1] * (point - x[i - 1]))
        result = np.dot(temp, coefficients)
        res.append(result)
    return res


# 绘制牛顿插值以及三次样样条插值的函数
def plot_interpolation(x, y):
    points = np.linspace(min(x), max(x), num=100)
    # 牛顿插值的结果
    y_interp_newton = newton_interpolation(x, y, points)
    # 标注库三次样条插值的结果
    y_interp_cubic = interp1d(x, y, kind="cubic")(points)
    y_oringin = 1 / (points**2 + 1)

    plt.plot(x, y, "ro", label="Original Data")
    plt.plot(points, y_interp_cubic, label="Curve (Cubic) Interpolation")
    plt.plot(points, y_interp_newton, label="Newton Interpolation")
    plt.plot(points, y_oringin, label="Original function")

    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


def main():
    x = [-2, -1, 0, 2, 3]
    y = [0.2, 0.5, 1, 0.2, 0.1]
    # print(newton_interpolation(x, y, x))
    plot_interpolation(x, y)


if __name__ == "__main__":
    main()
