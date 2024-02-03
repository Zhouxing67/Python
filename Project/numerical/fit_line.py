import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def exponential_func(x, a, b):
    return a * np.exp(b * x)


def get_fit_params(x, y):
    params, _ = curve_fit(exponential_func, x, y)
    # y = exponential_func(x, *params)
    return params


def plot_line(x, y, params):
    plt.scatter(x, y, label="Data")
    newx = np.arange(x[0] - 1, x[-1] + 1, 0.1)
    newy = exponential_func(newx, *params)
    plt.plot(newx, newy, "r-", label="Fitted curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


def main():
    x = np.arange(1, 5, 1)
    y = np.array([60, 30, 20, 15])

    params = get_fit_params(x, y)
    plot_line(x, y, params)


if __name__ == "__main__":
    main()
