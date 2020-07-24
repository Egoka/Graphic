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
    for h in range(border, size_image[0] - border):  # height
        for w in range(border, size_image[1] - border):  # width
            arr_pixels, center_pixel_sum = [], 0
            for h_min in range(-border, border + 1):
                for w_min in range(-border, border + 1):
                    r, g, b = int(image[h + h_min][w + w_min][0]), \
                              int(image[h + h_min][w + w_min][1]), \
                              int(image[h + h_min][w + w_min][2])
                    sum_color = (r + g + b)
                    if h_min == 0 and w_min == 0:
                        center_pixel_sum = sum_color
                    pixel = [r, g, b, sum_color]
                    arr_pixels.append(pixel)
                    del pixel, r, g, b, sum_color
            del h_min, w_min
            arr_pixels = sorted(arr_pixels, key=lambda point: (point[3], point[0], point[1], point[2]))
            factor = 0
            if math.fabs(arr_pixels[k][3] - center_pixel_sum) < math.fabs(arr_pixels[l][3] - center_pixel_sum):
                factor = k
            elif math.fabs(arr_pixels[k][3] - center_pixel_sum) >= math.fabs(arr_pixels[l][3] - center_pixel_sum):
                factor = l
            arr_pixels[factor].pop(3)
    return image