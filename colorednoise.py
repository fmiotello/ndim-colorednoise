import numpy as np

def generate_noise(size, beta):
    white_noise = np.random.randn(*size)
    white_noise_fft = np.fft.fftn(white_noise)

    ndims = len(size)
    freq_along_axis = []

    for axis in range(ndims):
      freq_along_axis.append(np.fft.fftfreq(size[axis]))

    grids = np.meshgrid(*freq_along_axis)
    sum_of_squares = 0

    for grid in grids:
      sum_of_squares += grid**2

    freqs = np.sqrt(sum_of_squares)
    origin = (0,) * ndims
    freqs[origin] += 1e-8      # DC component
    filter = 1/np.power(freqs, beta)

    colored_fft = white_fft * filter
    colored_noise = np.fft.ifftn(colored_fft)

    return np.abs(colored_noise)
