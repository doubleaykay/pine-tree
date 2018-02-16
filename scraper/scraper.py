from lxml import html
import requests

def print_class():
  # Initializes class number at 1
   class_number = 1
   while class_number <= 100:
    # Grabs the info from the page
       page = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry/CHEM-Chemistry-Undergraduate/CHEM-' + str(class_number))
       class_number += 1
       tree = html.fromstring(page.content)
       prereq = tree.xpath('//a[@class="sc-courselink"]/text()')
       print(prereq)
   #page = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry/CHEM-Chemistry-Undergraduate/CHEM-' + str(x))
   
   
   #title = tree.xpath('//span/text()')
   
   #print(title)

print_class()
