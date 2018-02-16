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
       title = tree.xpath('//span/text()')
       if title:
          title.remove('\r\n\r\n\t')
          title.remove(' >\r\n')
          title.remove('\r\n\r\n\r\n')
          prereq = tree.xpath('//a[@class="sc-courselink"]/text()')
          print('T:' + str(title))
          print(prereq)
       
print_class()
