import math
import matplotlib.pyplot as plt
i = []
for k in range (1, 1001):
    i.append(k)
x = []
for j in i:
    x.append( 20 * math.cos(2*math.pi*j + math.pi*0.12))

plt.plot(x)