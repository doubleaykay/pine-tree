from lxml import html
import requests
import re

#import list of course links
import links

f = open("nodes.js", "w")
f2 = open("edges.js", "w")

f.write("nodes=[\n")
f2.write("edges=[\n")

i = 1

# Grabs the info from the page
for link in links.links:
	page = requests.get(link)
	tree = html.fromstring(page.content)
	title = tree.xpath('//h1/span/text()')
	if title:
	  fulltitle = re.findall(r'\b.*\b',tree.xpath('//h1/span/following-sibling::text()')[0])[0]
	  title = title[0]
	  prereqs = tree.xpath('//div[@id="main"]/node()[count(preceding-sibling::h3[contains(text(),"Prerequisite")]) = 1]/descendant-or-self::text()')
	  pstring = "".join(prereqs[0:len(prereqs)-1])
	  pres = re.findall(r'[A-Z]{2,}\s\d*[.]?\d+',pstring)
	  offeredtexts = tree.xpath('//h3[text()="Offered"]/following-sibling::text()')
	  if offeredtexts:
	  	offered = re.findall(r'\d\d\w',offeredtexts[0])
	  else:
	  	offered = []
	  distribtexts = tree.xpath('//h3[contains(text(),"Distributive")]/following-sibling::text()')
	  if distribtexts:
	  	distribs = re.findall(r'(?<!=[A-Z,a-z])[A-Z]+(?!=[A-Z,a-z])', distribtexts[0])
	  else:
	  	distribs = []
	  print(title)
	  print(fulltitle)
	  print(pres)
	  print(offered)
	  print(distribs)
	  #print prereqs
	  #print offeredtexts
	  #print distribtexts
	  f.write('{ data: { id: "')
	  f.write(str(title.encode('utf-8')))
	  f.write('", class: "')
	  f.write(str(title.encode('utf-8')))
	  f.write('", title: \'')
	  f.write(str(fulltitle.encode('utf-8')).replace("'", "\\'").replace('"', '\\"'))
	  f.write('\', prereqs: ')
	  f.write(str(str(pres).encode('utf-8')))
	  f.write(', distribs: ')
	  f.write(str(str(distribs).encode('utf-8')))
	  f.write(', offered: ')
	  f.write(str(str(offered).encode('utf-8')))
	  f.write("}},\n")
	  #write to edge file
	  for pre in pres:
	  	f2.write("{ data: { id: '"+str(i)+"', source: '"+str(pre.encode('utf-8'))+"', target: '"+str(title.encode('utf-8'))+"' } },\n")
	  	i += 1



f.write("]")
f2.write("]")

f.close()
