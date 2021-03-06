from lxml import html
import requests

def getTree(link):
	return html.fromstring(requests.get(link).content)

# Grabs the info from the page
tree = getTree('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate?getchildren=1')

links = tree.xpath('//a/@href')


f = open("links.py", "w")

f.write("links = [\n")

for link in links:
	deptlinktree = getTree('http://dartmouth.smartcatalogiq.com'+link+'?getchildren=1')
	deptlinks = deptlinktree.xpath('//a/@href');
	for link in deptlinks:
		depttree = getTree('http://dartmouth.smartcatalogiq.com'+link+'?getchildren=1')
		courselinks = depttree.xpath('//a/@href')
		print courselinks
		for l in courselinks:
			f.write('"http://dartmouth.smartcatalogiq.com'+l+'",'+'\n')

f.write("]")
f.close()