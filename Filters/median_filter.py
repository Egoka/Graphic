def filter_median(image):
    size_image = image.shape
    column, row, arr_window = 1, 1, []
    while size_image[0] - 1 != column:
        while size_image[1] - 1 != row:
            i = -1
            while i != 2:
                j = -1
                while j != 2:
                    sum_color, elements, pix = 0, 0, []
                    while size_image[2] != elements:
                        sum_color += image[column + i][row + j][elements]
                        pix.append(image[column + i][row + j][elements])
                        elements += 1
                    pix.append(sum_color)
                    arr_window.append(pix)
                    j += 1
                i += 1
            row += 1
        column += 1
    return image