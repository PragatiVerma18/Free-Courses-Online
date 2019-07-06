import requests
from bs4 import BeautifulSoup
from csv import writer

webpage_response = requests.get('https://www.classcentral.com/report/free-for-credit-moocs/')

webpage = webpage_response.content
soup = BeautifulSoup(webpage,"html.parser")

headings = soup.findAll('h1')


with open('courses.csv', 'w', encoding="utf-8") as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Heading', 'Subheading', 'Link']
  csv_writer.writerow(headers)

  for i in range(1,len(headings)):
    href =[]
    text = []
    heading = headings[i].get_text()
    subheading = headings[i].find_next_sibling('h3').get_text()
    ul = headings[i].find_next_sibling('ul')
    children = ul.findChildren("li" , recursive=False)
    for child in children:
      href.append(child.findChildren('a')[0]['href'])
      text.append(child.get_text())
    link = dict(zip(href, text))
    csv_writer.writerow([heading, subheading, link])

 