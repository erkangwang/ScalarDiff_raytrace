import numpy as np

#u1: source plane field
#L1, source plane side length
#lamda: illumination wavelength
#f: focal length
def FT_prop(u1, L1, lamda, f):
    M = u1.shape[0]
    N = u1.shape[1]
    # source sample interval
    dx1 = L1 / (M - 1)
    dy1 = L1 / (N - 1)
    k = 2 * np.pi / lamda
    # define observation plane size and sample intervals
    L2 = lamda * f / dx1
    x2 = np.linspace(-L2/2, L2/2, M)
    y2 = np.linspace(-L2/2, L2/2, N)
    Xi, Yi = np.meshgrid(x2, y2)
    Chirp_Phase = 1 / (1j * lamda * f) * np.exp(1j * k / (2*f) * (Xi**2 + Yi**2))
    #u2 = Chirp_Phase * np.fft.fft2(np.fft.fftshift(u1)) * dx1 * dy1
    u2 = np.fft.fft2(u1)
    u2 = np.fft.fftshift(u2) * dx1 * dy1 * Chirp_Phase
    return u2, x2, y2, L2