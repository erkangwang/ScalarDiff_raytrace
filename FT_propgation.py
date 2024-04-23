import numpy as np

#u1: source plane field
#L1, source plane side length
#lamda: illumination wavelength
#f: focal length
def FT_prop(u, L, lamda, f):
    M = u.shape[0]
    N = u.shape[1]
    # source sample interval
    dx = L / (M - 1)
    dy = L / (N - 1)
    k = 2 * np.pi / lamda
    # define observation plane size and sample intervals
    Lout = lamda * f / dx
    xout = np.linspace(-Lout/2, Lout/2, M)
    yout = np.linspace(-Lout/2, Lout/2, N)
    #Xi, Yi = np.meshgrid(xout, yout)
    #Chirp_Phase = 1 / (1j * lamda * f) * np.exp(1j * k / (2*f) * (Xi**2 + Yi**2))
    Chirp_Phase = 1

    uout = np.fft.fftshift(u)
    uout = np.fft.fft2(uout)
    uout = np.fft.ifftshift(uout) * dx * dy * Chirp_Phase  #np.fft.fft2(uout) * dx * dy * Chirp_Phase
    return uout, xout, yout, Lout