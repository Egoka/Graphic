from skimage import io
from Filters.rank_filter import filter_rank
from Filters.median_filter import filter_median


def start_filter():
    image = io.imread('Photo/Photo_1.png')


if __name__ == '__main__':
    start_filter()