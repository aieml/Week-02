from sklearn.linear_model import LinearRegression
import numpy as np
import random

x=np.arange(0,10,1)
y=x+(x**2)+5

y1=[]

for i in y:

    y1.append(i+random.randint(-2,2))

y1=np.array(y1)

from matplotlib import pyplot as plt

plt.scatter(x,y1)
plt.plot(x,y,'r')
plt.show()
