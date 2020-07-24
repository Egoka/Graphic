import math


def filter_rank(image):
    size_image = image.shape
    n_size = int(input('Введите размер окна (нечетное): '))
    k_factor = int(input('Введите коэффициент выборки (от 0% до 100%):'))
    border = math.floor(n_size / 2)
    k = int((n_size ** 2) * (k_factor / 100))
    if k_factor == 100:
        l = int((n_size ** 2) - k)
        k -= 1
    else: l = int((n_size ** 2) - k - 1)
    del k_factor, n_size
    return image