# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
# Use https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions


import requests
import re
from bs4 import BeautifulSoup

print
print (" - ....working......")
print

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

# Part 1
student = soup.find_all(text = re.compile('student'))
for word in student:
    fixed_text = str(word).replace('student', 'AMAZING student')
    word.replace_with(fixed_text)

## Part 2 
for link in soup.findAll('iframe'):
	link['src'] = "/Users/JBone/documents/soccer.jpg"

### Part 3
for img in soup.findAll('img'):
	img['src'] = "/Users/JBone/documents/Fall 2016/SI 206/SI206/HW3-StudentCopy/media/logo.png"

text_file = open("Hw3Soupnew.html", "w")
print('Outputting html file....')
text_file.write(str(soup))
text_file.close()
print('Done')
