from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.microsoft.com/en-us/learning/mcse-certification.aspx').text

soup=BeautifulSoup(source,'lxml')

print(soup.prettify())
