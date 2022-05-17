#scraps all of the text off a website 
import urllib
import requests
import bs4

a_website = urllib.request.urlopen("http://www.kite.com/")
a_soup = bs4.BeautifulSoup(a_website)
website_text = a_soup.findAll(text = True)
print(website_text)