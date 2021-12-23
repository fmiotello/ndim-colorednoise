import numpy as np

def generate_noise(size, beta):
    white_noise = np.random.randn(*size)
    white_noise_fft = np.fft.fft2(white)

    f_along_x = np.fft.fftfreq(size[0])
    f_along_y = np.fft.fftfreq(size[1])

    grid1, grid2 = np.meshgrid(f_along_x, f_along_y)
    freqs = np.sqrt(grid1**2 + grid2**2)
    freqs[0,0] += 1e-8      # DC component
    filter = 1/np.power(freqs, beta)

    colored_fft = white_fft * filter
    color = np.fft.ifft2(colored_fft)

    return color
