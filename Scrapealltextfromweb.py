# Website to use: https://www.onetonline.org/ 
# example website: https://www.onetonline.org/link/summary/25-1021.00

"""
Description:
This will take all the etx from the desired website and make it into a pdf for it to merg
"""

#Libraries 
import urllib
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF


################################################SCRAPPING TEXT FROM A WEBSITE
# asks the user which website to take all the text from 
#website = input("what website would you like to scrape? ")

website = "https://www.onetonline.org/link/summary/25-1021.00"

# getting response object
res = requests.get(website)
 
# Initialize the object with the document
soup = BeautifulSoup(res.content, "html.parser")
 
# Get the whole body tag
tag = soup.div
lis = [] 


# Puts each div text in a list and strips of unessary test
for string in tag.strings:
    lis.append(string.rstrip("\n"))


# allows us to print out the binary into the pdf
restext = list(filter(None, lis))
text = [x.encode('utf-8') for x in restext]


################################################Creation of the pdf
#creates the pdf 
pdf = FPDF('P', 'mm', 'Letter')

#Adds a page 
pdf.add_page()

#spefify the font and color
pdf.set_font('times', '', 1)

##creates the watermark for the paper
watermark = "" 
for i in text:
    watermark += str(i) + " "

# repeats three times (for the ATS to notice it)
for j in range(3):
    pdf.multi_cell(0, .5, watermark)

#outputs the pdf
pdf.output('watermark.pdf')


