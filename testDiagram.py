#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

"""t = np.arange(1, 1000, 1)
s = np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('term''s'' rank')
plt.ylabel('frequency (10)')
plt.title('a diagram for frequency of a term')
plt.grid(True)
plt.savefig("test.png")
plt.show()"""
x=[x for x in range(1,100)]
y=[y for y in range(100,10000,100)]
plt.plot(x,y)
plt.show()
