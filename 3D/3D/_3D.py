import matplotlib.pyplot as plt
import numpy

def calculate_ellip_paraboloid ():
    x = numpy.linspace (-10, 10, 25)
    y = numpy.linspace (-10, 10, 25)

    xgrid, ygrid = numpy.meshgrid(x, y)

    z = xgrid**2 + ygrid**2
    return xgrid, ygrid, z

def calculate_hyper_paraboloid ():
    x = numpy.linspace (-10, 10, 25)
    y = numpy.linspace (-10, 10, 25)

    xgrid, ygrid = numpy.meshgrid(x, y)

    z = xgrid**2 - ygrid**2
    return xgrid, ygrid, z


if __name__ == '__main__':
    x1, y1, z1 = calculate_ellip_paraboloid()

    fig_1 = plt.figure()
    axes_1 = fig_1.add_subplot(projection='3d')

    x2, y2, z2 = calculate_hyper_paraboloid()
    fig_2 = plt.figure()
    axes_2 = fig_2.add_subplot(projection='3d')

    axes_1.plot_wireframe(x1, y1, z1, color='r')
    axes_2.plot_wireframe(x2, y2, z2, color='g')

    plt.show()
