import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(1, 100)
f1 = 8*x
f2 = (4*x) * np.log2(x)
f3 = 2*(x**2)
#f4 = 2**x
print(f2)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


plt.loglog(x, f1, 'r', label="8x")
plt.loglog(x, f2, 'g', label="4x log x")
plt.loglog(x, f3, 'b', label="2x^2")
#plt.loglog(x, f4, 'black', label="2^x")

plt.legend()
plt.show()
