import numpy as np
import matplotlib.pyplot as plt

# INPUT
T_1 = 350.0 # [K]
T_2 = 300.0 # [K]

r_1 = 0.3 # [m]
r_2 = 0.5 # [m]



r = np.linspace(r_1, r_2, 100)

# Plate
s = r_2 - r_1
T = (r_2 - r)/s *(T_1 - T_2) + T_2
plt.plot(r, T, label='plate')

# Cylinder
T = np.log(r_2 / r) / np.log(r_2 / r_1) * (T_1 - T_2) + T_2
plt.plot(r, T, label='Cylinder')

# Sphere
T = (1/r - 1/r_2) / (1/r_1 - 1/r_2) * (T_1 - T_2) + T_2
plt.plot(r, T, label='Cylinder')

plt.xlabel('r [m]')
plt.ylabel('T [K]')
plt.legend()
plt.tight_layout()
plt.show()
