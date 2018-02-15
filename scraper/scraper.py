from lxml import html
import requests

def print_class():
  # Initializes class number at 1
   class_number = 1
   while class_number <= 100:
    # Grabs the info from the page
       page = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry/CHEM-Chemistry-Undergraduate/CHEM-' + str(class_number))
       class_number += 1
   #page = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry/CHEM-Chemistry-Undergraduate/CHEM-' + str(x))
   tree = html.fromstring(page.content)
   prereq = tree.xpath('//a[@class="sc-courselink"]/text()')
   title = tree.xpath('//span/text()')
   print(prereq)
   #print(title)

print_class()
