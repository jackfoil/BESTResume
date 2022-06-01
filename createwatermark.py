"""
Description:
This will take all the spoecific words from the desired websites and create a pdf 
(this will be the watermark page)
"""

#Libraries 
import urllib
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF


################################################SCRAPPING TEXT FROM A WEBSITE
# asks the user which website to take all the text from 
#website = input("what website would you like to scrape? ")


def createwatermark(website, num, numlimit):
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
    #pdf.set_text_color(255,255,255)

    ##creates the watermark for the paper
    watermark = "" 
    limit = 0
    for i in text:
        watermark += str(i) + " "
        limit += 1
        if(limit > numlimit):
            break

    # repeats three times (for the ATS to notice it)
    for j in range(num):
        pdf.multi_cell(0, .75, watermark)

    #outputs the pdf
    pdf.output('Testpdfs/watermark.pdf')




if __name__ == "__main__":
    createwatermark("https://www.onetonline.org/link/summary/25-1021.00", 3, 200)




