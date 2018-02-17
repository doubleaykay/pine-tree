from lxml import html
import requests

#import list of course links
import links

def print_class():
    # Grabs the info from the page
    for link in links.links:
       page = requests.get(link)
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
