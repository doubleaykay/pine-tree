from lxml import html
import requests
import re

#import list of course links
import links

def print_class():
    # Grabs the info from the page
    #for link in links.links:
       page = requests.get('http://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Computer-Science/COSC-Computer-Science-Undergraduate/COSC-74')
       tree = html.fromstring(page.content)
       title = tree.xpath('//span/text()')
       if title:
          title.remove('\r\n\r\n\t')
          title.remove(' >\r\n')
          title.remove('\r\n\r\n\r\n')
          #prereqs = tree.xpath('//a[@class="sc-courselink"]/text()')
          #prereqs = tree.xpath('//h3[text()[contains(.,"Prerequisite")]]/following-sibling::node()/descendant-or-self::text()')
          prereqs = tree.xpath('//div[@id="main"]/node()[count(preceding-sibling::h3) = 1]/descendant-or-self::text()')
          pstring = "".join(prereqs[0:len(prereqs)-1])
          print('T:' + str(title))
          print(pstring)
          print re.findall(r'[A-Z]{2,}\W+\d*\d',pstring)
          
print_class()
