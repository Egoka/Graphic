from skimage import io
from Filters.rank_filter import filter_rank
from Filters.median_filter import filter_median


def start_filter():
    image = io.imread('Photo/Photo_1.png')
    image_rank = filter_rank(image)
    io.imsave('Photo/Filter_rank.png', image_rank)
    view(image_rank)
    image_median = filter_median(image)
    io.imsave('Photo/Filter_median.png', image_median)
    view(image_median)


def view(image):
    io.imshow(image)
    io.show()


if __name__ == '__main__':
    start_filter()