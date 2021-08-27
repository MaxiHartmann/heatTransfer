import matplotlib.pyplot as plt
import numpy as np

# INPUTS
Q = 20 # [W]
T_i = 350 # [K]

def calc_Area(r):
    return np.pi * r * r

# assumption:
T_iw = T_i

r_1i = 0.1      # [m]
s1 = 0.01       # [m]
s2 = 0.01       # [m]
s3 = 0.01       # [m]

alpha_i = 1e9   # [W/m2K]
alpha_a = 25     # [W/m2K]

# thermal conductivity
lambda_1 = 17   # [W/(mK)] 
lambda_2 = 0.03 # [W/(mK)] 
lambda_3 = 17   # [W/(mK)] 

r_1a = r_1i + s1
r_2i = r_1a
r_2a = r_2i + s2
r_3i = r_2a
r_3a = r_3i + s3

height = 1      # [m]

R_th1 = np.log(r_1a - r_1i) / (2 * np.pi * height * lambda_1)


plt.plot([r_1i, r_1i, r_2i, r_2i], [0, 400, 400, 0], color='blue', linewidth=2, label='layer 1')
plt.plot([r_3i, r_3i, r_3a, r_3a], [0, 400, 400, 0], color='blue', linewidth=2, label='layer 3')
plt.plot([r_2i, r_2i, r_3i, r_3i], [0, 400, 400, 0], color='red', linewidth=1, label='layer 2')
plt.legend()
plt.xlim(0, 0.2)
plt.ylim(270, 370)

r_1 = np.linspace(r_1i, r_1a, 20)
T_1 = T_iw - Q/(lambda_1 * 2 * np.pi * height) * np.log(r_1 / r_1i)
plt.plot(r_1, T_1, label='T(r)')

r_2 = np.linspace(r_2i, r_2a, 20)
T_2 = T_1[-1] - Q/(lambda_2 * 2 * np.pi * height) * np.log(r_2 / r_2i)
plt.plot(r_2, T_2, label='T(r)')

r_3 = np.linspace(r_3i, r_3a, 20)
T_3 = T_2[-1] - Q/(lambda_3 * 2 * np.pi * height) * np.log(r_3 / r_3i)
plt.plot(r_3, T_3, label='T(r)')
r_w = r_3a

q = Q/(np.pi * r_w * r_w)
T_inf = T_3[-1] - q / alpha_a
plt.plot([r_3[-1], 2*r_3[-1]], [T_inf, T_inf], label='T_inf')

# alpha = lambda_lam_air / thickness_T
lambda_lam_air = 0.02572 # [W/(mK)]
thickness_T = lambda_lam_air / alpha_a
print("thermal boundary layer thickness = {:.5f} m".format(thickness_T))


# TODO: profile of T in boundary layer...
# alpha_i, alpha_a
# ...

plt.xlabel('radius [m]')
plt.ylabel('temperature [K]')
plt.show()
