import kabsch
import numpy as np
import csv


def main():
    A = kabsch.read_data("A.csv")
    B = kabsch.read_data("B.csv")
    R, T = kabsch.kabsch1(A, B)
    B_ = np.dot(R, A.T).T + T
    miss = B - B_
    with open("miss.csv", "w+", newline="") as miss_file:
        writer = csv.writer(miss_file)
        writer.writerows(miss)
    print(f'旋转矩阵：{R}')
    print(f'平移距离：{T}')
    kabsch.plot_3d_points(A, B, B_)


if __name__ == "__main__":
    main()
