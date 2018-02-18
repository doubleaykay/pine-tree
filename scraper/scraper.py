from lxml import html
import requests
import re

#import list of course links
import links

f = open("nodes.js", "w")

f.write("'nodes':[\n")

# Grabs the info from the page
#for link in links.links:
page = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Latin-American-Latino-and-Caribbean-Studies/LACS-Latin-American-and-Caribbean-Studies/LACS-50-13')
tree = html.fromstring(page.content)
title = tree.xpath('//h1/span/text()')
fulltitle = re.findall(r'\b.*\b',tree.xpath('//h1/span/following-sibling::text()')[0])[0]
if title:
  title = title[0]
  prereqs = tree.xpath('//div[@id="main"]/node()[count(preceding-sibling::h3) = 1]/descendant-or-self::text()')
  pstring = "".join(prereqs[0:len(prereqs)-1])
  pres = re.findall(r'[A-Z]{2,}\s\d+[.]?\d+',pstring)
  offered = re.findall(r'\d\d\w',tree.xpath('//h3[text()="Offered"]/following-sibling::text()')[0])
  distribs = re.findall(r'(?<=\W)[A-Z]+?(?=\W)'," ".join([tree.xpath('//h3[contains(text(),"Distributive")]/following-sibling::text()')[0]," "]))
  print(title)
  print(fulltitle)
  print(pres)
  print(offered)
  print(distribs)
  f.write('{ "data": { "id": "')
  f.write(title)
  f.write('", "class": "')
  f.write(title)
  f.write('", "title": "')
  f.write(fulltitle)
  f.write('", "prereqs": ')
  f.write(str(pres))
  f.write(', "distribs": ')
  f.write(str(distribs))
  f.write(', "offered": ')
  f.write(str(offered))
  f.write("}},\n")


f.write("]")

f.close()