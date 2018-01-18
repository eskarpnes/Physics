import matplotlib.pyplot as plotter
import numpy

x = numpy.linspace(-5, 5, 100)
f = x**2

plotter.plot(x, f, label=r'$x^2$')
plotter.legend()
plotter.title('Parabel')
plotter.xlabel('x')
plotter.ylabel('y')
plotter.show()
