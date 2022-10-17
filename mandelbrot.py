import math
import numpy
import matplotlib.pyplot as plt


# function to test if a given point is in the mandelbrot set, returns a boolean value
def in_mandelbrot(xx, yy, N_max, threshold):
    c = xx + 1j * yy

    z = 0
    for j in range(N_max):
        z = z ** 2 + c
        distance = math.sqrt(z.real ** 2 + z.imag ** 2)
        if distance > threshold:
            return False
    return True


def mandelbrot(n, threshold, N_max):


    xvalues = []
    yvalues = []

    # n is the resolution of our grid

    # fill vectors with x values between [-2 and 1] and y values between [-1.5 and 1.5]
    for i in range(n):
        xvalues.append(-2 + i / (n / 3))
        yvalues.append(-1.5 + i / (n / 3))

    # create mesh grid
    x, y = numpy.meshgrid(xvalues, yvalues)



    # creates 2d boolean array with the size being the resolution filled with false
    mask = [[False for i in range(n)] for j in range(n)]

    # for all x values
    for i in range(n):
        # for all y values
        for j in range(n):
            # check if given point is in mandelbrot set

            if in_mandelbrot(xvalues[i], yvalues[j], N_max, threshold):
                mask[j][i] = True

    # creates the image using given code
    plt.imshow(mask, extent=[-2,  1, -1.5, 1.5])
    plt.gray()
    plt.savefig(' mandelbrot.png')

mandelbrot(1000, 10, 30)