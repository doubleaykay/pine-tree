from lxml import html
import requests
page = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry/CHEM-Chemistry-Undergraduate/CHEM-75')
tree = html.fromstring(page.content)
prereq = tree.xpath('//a[@class="sc-courselink"]/text()')
title = tree.xpath('//span/text()')
print(prereq)
print(title)
