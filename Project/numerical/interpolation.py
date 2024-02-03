import matplotlib.pyplot as plt
from fractions import Fraction


def divided_difference_table(x, f):
    rows = len(x)  # 行数
    cols = len(x) + 1  # 列数
    temp = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        temp[i][0] = Fraction(x[i])
        temp[i][1] = Fraction(f[i])
    for i in range(1, rows):
        for j in range(2, i + 2):
            temp[i][j] = (temp[i][j - 1] - temp[i - 1][j - 1]) / (
                temp[i][0] - temp[i - j + 1][0]
            )
    print("差商表为")
    for row in temp:
        print([str(Fraction(element).limit_denominator()) for element in row])


def main():
    x = [1, 2, 4, 7]
    f = [4, 1, 0, -1]
    plt.scatter(x, f, label="data")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    divided_difference_table(x, f)


if __name__ == "__main__":
    main()
