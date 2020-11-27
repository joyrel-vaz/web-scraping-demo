from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request, urlopen

req = Request("https://www.indianhealthyrecipes.com/post-sitemap1.xml")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "xml")
links = []

for link in soup.findAll('url'):
    links.append(link.loc.get_text())

print(links)    
df = pd.DataFrame(links, columns = ["RECIPE LINKS"])
df.to_csv('indianhealthyrecipes.csv' , index = False)
print('Number of links = {}'.format(len(links)))