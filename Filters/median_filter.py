def filter_median(image):
    size_image = image.shape
    column, row = 1, 1
    while size_image[0] - 1 != column:
        while size_image[1] - 1 != row:
            i = -1
            while i != 2:
                j = -1
                while j != 2:
                    sum_color, elements, pix = 0, 0, []
                    j += 1
                i += 1
            row += 1
        column += 1
    return image