from lxml import html
import requests
import re

#import list of course links
import links

# Grabs the info from the page
#for link in links.links:
page = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Computer-Science/COSC-Computer-Science-Undergraduate/COSC-74')
tree = html.fromstring(page.content)
title = tree.xpath('//h1/span/text()')
fulltitle = re.findall(r'\b.*\b',tree.xpath('//h1/span/following-sibling::text()')[0])[0]
if title:
  prereqs = tree.xpath('//div[@id="main"]/node()[count(preceding-sibling::h3) = 1]/descendant-or-self::text()')
  pstring = "".join(prereqs[0:len(prereqs)-1])
  offered = re.findall(r'\d\d\w',tree.xpath('//h3[text()="Offered"]/following-sibling::text()')[0])
  distrib = re.findall(r'[A-Z]+',tree.xpath('//h3[contains(text(),"Distributive")]/following-sibling::text()')[0])
  print(title[0])
  print(fulltitle)
  print(re.findall(r'[A-Z]{2,}\W+\d*\d',pstring))
  print(offered)
  print(distrib)