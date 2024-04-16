import numpy as np
import FT_propgation as FTP
import matplotlib.pyplot as plt
import random
from photutils.aperture import CircularAperture

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Fourier transform based ray tracing')


# create meshgrid space for spatial and frequency domain
nx = 101
ny = 101
L1 = 200    #um
lamda = 0.5 #um
f = 1000     #um
x = np.linspace(-L1/2, L1/2, nx)
dx = x[1]-x[0]
y = np.linspace(-L1/2, L1/2, ny)
dy = y[1]-y[0]
Xo, Yo = np.meshgrid(x, y)

# on axis plan wave illuminate an aperture
R=80
circ_aper = np.sqrt(Xo**2 + Yo**2) <= R
u1 = circ_aper
out, x2, y2, L2 = FTP.FT_prop(u1, L1, lamda, f)

plt.subplot(421)
image = plt.imshow(np.abs(u1), extent=[-L1/2,L1/2,-L1/2,L1/2])
plt.xlabel('x1 um')
plt.ylabel('y1 um')
plt.subplot(422)
image = plt.imshow(np.abs(out), extent=[-L2/2,L2/2,-L2/2,L2/2])
plt.xlabel('x2 um')
plt.ylabel('y2 um')


# Gaussian shaped aperture illuminated by on-axis plane wave
def gaus2d(x=0, y=0, mx=0, my=0, sx=20, sy=20):
    return 1. / (2. * np.pi * sx * sy) * np.exp(-((x - mx)**2. / (2. * sx**2.) + (y - my)**2. / (2. * sy**2.)))
u1 = gaus2d(Xo, Yo)
out, x2, y2, L2 = FTP.FT_prop(u1, L1, lamda, f)
# after the FT, the horizontal and vertical axis are spatial freq fx=x2/(lamda*f) fy=y2/(lamda*f)
# always need conversion
plt.subplot(423)
image = plt.imshow(np.abs(u1), extent=[-L1/2,L1/2,-L1/2,L1/2])
plt.xlabel('x1 um')
plt.ylabel('y1 um')
plt.subplot(424)
image = plt.imshow(np.abs(out), extent=[-L2/2,L2/2,-L2/2,L2/2])
plt.xlabel('x2 um')
plt.ylabel('y2 um')


# sine grating illuminated by on-axis plane wave
u1 = np.sin(Xo/10)
out, x2, y2, L2 = FTP.FT_prop(u1, L1, lamda, f)
# after the FT, the horizontal and vertical axis are spatial freq fx=x2/(lamda*f) fy=y2/(lamda*f)
# always need conversion
plt.subplot(425)
image = plt.imshow(np.abs(u1), extent=[-L1/2,L1/2,-L1/2,L1/2])
plt.xlabel('x1 um')
plt.ylabel('y1 um')
plt.subplot(426)
image = plt.imshow(np.abs(out), extent=[-L2/2,L2/2,-L2/2,L2/2])
plt.xlabel('x2 um')
plt.ylabel('y2 um')


# sine grating illuminated by a plane wave with a illumination angle
Xi = 1/60
Eta = 0
#Zeta =
u1 = np.sin(Xo/10) * np.exp(1j * 2 * np.pi * Xi * Xo) * np.exp(1j * 2 * np.pi * Eta * Yo)
#u1 = np.exp(1j * 2 * np.pi * Xi * Xo) * np.exp(1j * 2 * np.pi * Eta * Yo)
out, x2, y2, L2 = FTP.FT_prop(u1, L1, lamda, f)
# after the FT, the horizontal and vertical axis are spatial freq fx=x2/(lamda*f) fy=y2/(lamda*f)
# always need conversion
plt.subplot(427)
image = plt.imshow(np.real(u1), extent=[-L1/2,L1/2,-L1/2,L1/2])
plt.xlabel('x1 um')
plt.ylabel('y1 um')
plt.subplot(428)
image = plt.imshow(np.abs(out), extent=[-L2/2,L2/2,-L2/2,L2/2])
plt.xlabel('x2 um')
plt.ylabel('y2 um')
plt.show()