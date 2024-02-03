import numpy as np


def main():
    A = np.array(
        [
            [0.8147, 0.0975, 0.1576, 0.1419, 0.6557],
            [0.9058, 0.2785, 0.9706, 0.4218, 0.0357],
            [0.127 * 10**10, 0.5469, 0.9572, 0.9157, 0.8491],
            [0.9134, 0.9575, 0.4854 * 10**8, 0.7922 * 10**300, 0.9340],
            [0.6324, 0.9649, 0.8003, 0.9595, 0.6787],
        ]
    )

    b = np.array(
        [
            1.0e09 * 0.000000002258000,
            1.0e09 * 0.000000001597700,
            1.0e09 * 1.270000002354900,
            1.0e09 * 0.024270003904200,
            1.0e09 * 0.000000003360250,
        ]
    )
    x = gauss_elimination(A, b)
    print(x)

    x = np.linalg.solve(A, b)
    print(x)


def gauss_elimination(A, b):
    """
    列主元高斯消元法求解线性方程组 Ax = b

    参数：
    A: 系数矩阵，numpy数组
    b: 常数向量，numpy数组

    返回值：
    x: 解向量，numpy数组
    """
    n = len(b)
    # 构造增广矩阵
    Ab = np.concatenate((A, b.reshape((n, 1))), axis=1)
    # 高斯消元
    for i in range(n - 1):
        # 选主元
        max_index = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_index]] = Ab[[max_index, i]]
        # 消元操作
        for j in range(i + 1, n):
            ratio = Ab[j, i] / Ab[i, i]
            Ab[j] -= ratio * Ab[i]
    # 回代求解
    x = np.zeros(n)
    x[-1] = Ab[-1, -1] / Ab[-1, -2]
    for i in range(n - 2, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i:n], x[i:n])) / Ab[i, i]
    return x


if __name__ == "__main__":
    main()
