#this will merge the resume and wateramrk together 
#source: https://robsiegwart.com/blog/merging-and-watermarking-pdf-files-with-python/

import sys
from pdfrw import PdfReader, PdfWriter, PageMerge


def merging(input_file, watermark_file):
    #takes two files from cmd argument 
    #input_file = sys.argv[1] #resume
    #watermark_file = sys.argv[2] #watermark

    input_pdf = PdfReader(input_file)
    watermark = PdfReader(watermark_file).pages[0]


    # puts the water mark on all of the pages 
    for page in input_pdf.pages:
        merger = PageMerge(page)
        merger.add(watermark).render()

    writer = PdfWriter()
    writer.write(input_file.split('.pdf')[0]+'_w.pdf',input_pdf)


if __name__ == "__main__":
    merging('Resume.pdf', 'watermark.pdf')
