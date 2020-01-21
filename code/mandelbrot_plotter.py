import cmath
import numpy as np
import matplotlib.pyplot as plt
import time

def mandelbrot_function(z, c):
    return z**2 + c

def mandelbrot(input_number):
    iterations = 0
    output = 0 
    z_value = 0
    while abs(output) < 2 and iterations < 50:
        output = mandelbrot_function(output, input_number)
        z_value = output
        iterations+=1
    if abs(output) >= 2:
        return iterations
    else:
        return 0

def frange(start, stop, step):
    i = start
    range_array = []
    while i < stop:
        range_array.append(i)
        i += step
    return range_array

start_time = time.time()
step = 0.005
x_range = frange(-2,1,step)
y_range = frange(-1.2,1.2,step)
mandelbrot_plot = np.zeros((len(y_range),len(x_range)))
for y_pos, j in enumerate(y_range):
    if y_pos == round(len(y_range)/10):
        print("10 percent complete")
    for x_pos, i in enumerate(x_range):
        value = mandelbrot(complex(i, j))
        mandelbrot_plot[y_pos,x_pos] = value

print("Time taken to generate (s): ", time.time()-start_time)

plt.imshow(mandelbrot_plot, cmap=plt.get_cmap('inferno'))
plt.show()