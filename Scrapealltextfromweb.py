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

# Print each string recursively
for string in tag.strings:
    lis.append(string)
    
quit()
################################################Creation of the pdf
#creates the pdf 
pdf = FPDF('P', 'mm', 'Letter')

#Adds a page 
pdf.add_page()

#spefify the font and color
pdf.set_font('times', '', 1)


#add text
pdf.multi_cell(0, 1, lis)
pdf.output('pdf_1.pdf')


