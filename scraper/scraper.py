from lxml import html
import requests
import re

#import list of course links
import links

f = open("nodes.js", "w")
f2 = open("edges.js", "w")

f.write("nodes:[\n")
f2.write("edges:[\n")

i = 1

# Grabs the info from the page
for link in links.links:
	page = requests.get(link)
	tree = html.fromstring(page.content)
	title = tree.xpath('//h1/span/text()')
	if title:
	  fulltitle = re.findall(r'\b.*\b',tree.xpath('//h1/span/following-sibling::text()')[0])[0]
	  title = title[0]
	  prereqs = tree.xpath('//div[@id="main"]/node()[count(preceding-sibling::h3) = 1]/descendant-or-self::text()')
	  pstring = "".join(prereqs[0:len(prereqs)-1])
	  pres = re.findall(r'[A-Z]{2,}\s\d+[.]?\d+',pstring)
	  offeredtexts = tree.xpath('//h3[text()="Offered"]/following-sibling::text()')
	  if offeredtexts:
	  	offered = re.findall(r'\d\d\w',offeredtexts[0])
	  else:
	  	offered = []
	  distribtexts = tree.xpath('//h3[contains(text(),"Distributive")]/following-sibling::text()')
	  if distribtexts:
	  	distribs = re.findall(r'(?<=\W)[A-Z]+?(?=\W)'," ".join([distribtexts[0]," "]))
	  else:
	  	distribs = []
	  print(title)
	  print(fulltitle)
	  print(pres)
	  print(offered)
	  print(distribs)
	  f.write('{ data: { id: "')
	  f.write(title)
	  f.write('", class: "')
	  f.write(title)
	  f.write('", title: "')
	  f.write(fulltitle)
	  f.write('", prereqs: ')
	  f.write(str(pres))
	  f.write(', distribs: ')
	  f.write(str(distribs))
	  f.write(', offered: ')
	  f.write(str(offered))
	  f.write("}},\n")
	  #write to edge file
	  for pre in pres:
	  	f2.write("{ data: { id: '"+str(i)+"', source: '"+pre+"', target: '"+title+"' } },\n")
	  	i += 1
	  if i > 100:
	  	break



f.write("]")
f2.write("]")

# Takes the nodes.js file and fixes the formatting to get rid of [, ], make it so the prereqs and distribs are 
# between single quotes like 'INT, LIT, CI', and double quotes are replaced with single quotes and puts it into nodes_2.js
file = "nodes.js"
f3 = open(file, "r")
f4 = open("nodes_2.js", "w")

for line in f3:
    new_line = line.replace("[", "")
    new_line = new_line.replace("]", "")
    new_line = new_line.replace("', '", ", ")
    new_line = new_line.replace('"', "'")
    print(new_line)
    f4.write(new_line)

f3.close()
f4.close()

f.close()
f2.close()
