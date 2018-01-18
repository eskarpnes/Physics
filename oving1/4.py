import numpy as np
import matplotlib.pyplot as plotter


def v(t):
    c1 = 3.0
    c2 = 0.8
    return (c1*t**2)/2 - (c2*t**4)/4

def car_plot(t):
    plotter.plot(t, v(t))
    plotter.show()


def areal(v, n):
    dt = 2.0/n
    ds = v*dt
    s = np.sum(ds[0:n-2])
    s_trap = 0.5*ds[0] + np.sum(ds[1:n-2]) + 0.5*ds[1]

    return s, s_trap


if __name__ == "__main__":
    n = 3000
    t = np.linspace(0, 2, n)
    car_plot(t)
    print(areal(v(t), n))

cd 
