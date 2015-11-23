import requests
import sys
from lxml import html
import re

url=""
arg=""

if(len(sys.argv)==3):
	url = sys.argv[1]
	arg = sys.argv[2]
else:
	url = raw_input("Enter the web address: ")
	arg = raw_input("Enter the term to search: ")

response = requests.get(url)
web_content = response.content

regex = "<a class=\"fk-display-block\" data-tracking-id=\"prd_title\" href=\"(.+?)\" title"
pattern=re.compile(regex)
web_blocks=re.findall(pattern,web_content)
print "The property " + arg + " is in: "
for block in web_blocks:
	block = 'http://www.flipkart.com' + block
	response = requests.get(block)
	tree = html.fromstring(response.content)
	specsKey = tree.xpath('//td[@class="specsKey"]/text()')
	specsValue = tree.xpath('//td[@class="specsValue"]/text()')
	for i in range(0,len(specsValue)):
		specsValue[i] = specsValue[i].strip().lower()
	for i in range(0,len(specsValue)-1):
		if(arg in specsValue[i]):
			print block
			print '\n'
			break