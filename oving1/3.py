import numpy as np
import matplotlib.pyplot as plotter

def sum_1_100():
    list = np.arange(1, 101, 1)
    list_sum = np.sum(list)
    return list_sum

def plot_func():
    w = 5
    a = 2
    t = np.linspace(0, 10, 100)
    f = np.cos(w*t)*np.exp(-a*t)
    plotter.plot(t, f)
    plotter.show()

if __name__ == "__main__":
    print(sum_1_100())
    plot_func()
