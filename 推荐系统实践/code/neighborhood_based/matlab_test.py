#!/usr/bin/python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import numpy as np

if __name__ == "__main__":
    """matlab"""
    xmin, xmax = -4, 4
    xx = np.linspace(xmin, xmax, 100)
    plt.plot([xmin, 0, 0, xmax], [1, 1, 0, 0], 'k-', label="Zero-one loss")
    plt.plot(xx, np.where(xx < 1, 1 - xx, 0), 'g-', label="Hinge loss")
    plt.plot(xx, np.log2(1 + np.exp(-xx)), 'r-', label="Log loss")
    plt.plot(xx, np.exp(-xx), 'c-', label="Exponential loss")
    plt.plot(xx, -np.minimum(xx, 0), 'm-', label="Perceptron loss")

    plt.ylim((0, 8))
    plt.legend(loc="upper right")
    plt.xlabel(r"Decision function $f(x)$")
    plt.ylabel("$L(y, f(x))$")
    plt.show()
