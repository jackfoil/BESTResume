#this is the main code (that I created)
from createwatermark import *
from merg import *
from frontend import *


if __name__ == "__main__":
    createwatermark("https://www.onetonline.org/link/summary/25-1021.00", 2, 200)
    merging('Testpdfs/Resume.pdf', 'Testpdfs/watermark.pdf')









