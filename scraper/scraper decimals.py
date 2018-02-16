from lxml import html
import requests

def print_class():
   # Classes with no decimal numbering
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
       if class_number == 100:
          break

   class_number_a = 92
   class_number_b = 1
   while class_number_a <= 100 and class_number_b <= 9:
      page2 = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry/CHEM-Chemistry-Undergraduate/CHEM-' + str(class_number_a) + '-' + '0' + str(class_number_b))
      class_number += 1
      tree2 = html.fromstring(page.content)
      title2 = tree2.xpath('//span/text()')
      if title2:
         title2.remove('\r\n\r\n\t')
         title2.remove(' >\r\n')
         title2.remove('\r\n\r\n\r\n')
         prereq2 = tree2.xpath('//a[@class="sc-courselink"]/text()')
         print('T:' + str(title2))
         print(prereq2)
   
print_class()
