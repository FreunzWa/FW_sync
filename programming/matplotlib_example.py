import matplotlib.pyplot as plt
import numpy as np

plt.title('Example graph')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
x = [-2,-1,0,1,2]
y = [4,1,0,1,4]
plt.plot(x,y,'sk--')
plt.xlim((-5,5))

plt.show()
