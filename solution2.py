import numpy as np
from math import exp
import matplotlib.pyplot as plt

def gaussian(x, mu, sigma):
  return exp(-(((x-mu) / (sigma))** 2) / 2.0)

def gauss_kernel(kernel_radius = 2, sigma = 10):
    # считаем элементы ядра
    h_kernel = [gaussian(x, kernel_radius, sigma) for x in range(2 * kernel_radius + 1)]
    v_kernel = [x for x in h_kernel]
    kernel_2d = [[xh * xv for xh in h_kernel] for xv in v_kernel]
    # нормализуем ядро
    kernel_sum = sum([sum(row) for row in kernel_2d])
    kernel_2d = [[x/kernel_sum for x in row] for row in kernel_2d]
    return np.array([np.array(xi) for xi in kernel_2d])

def gaussian_filter(img, windows_size):
    img2 = np.zeros_like(img)
    kernel = gauss_kernel()
    padding = windows_size//2
    for i in range(windows_size//2, img.shape[0] - windows_size//2):
        for j in range(windows_size//2, img.shape[1] - windows_size//2):
            for c in range(img.shape[2]):
                conv = img[i - padding:i + padding+1, j-padding:j+padding+1, c] * kernel
                img2[i, j, c] = conv.sum()

    return img2


img = plt.imread("cat.png")[:, :, :3]
img2 = gaussian_filter(img, 5)

fig, axs = plt.subplots(1, 2)
axs = axs.ravel()

axs[0].imshow(img)
axs[1].imshow(img2)
plt.show()