from datetime import datetime
from enum import Enum
from bs4 import BeautifulSoup

def start_scraping(page_source):
  # initialise bs
  soup = BeautifulSoup(page_source, "lxml")

  # Get rating
  rating = soup.find("div", {"class": "rating-number"}).contents[0]
  
  # Get activity table
  table = soup.find("table", {'class': 'dataTable'})

  # Get result of submission
  spans = table.find_all('span')
  results = []
  for span in spans:
    results.append(span['title'] or 'accepted')

  # Get name of all problems
  problems = [link.contents[0] for link in table.find_all('a')]

  # Get name of language used
  all_tds = table.find_all('td')
  languages = []
  for i in range(3, len(all_tds), 4):
    languages += [all_tds[i].contents[0]]

  # Get time of submission used
  times = []
  for i in range(0, len(all_tds), 4):
    try:
      times += [datetime.strptime(all_tds[i].contents[0], '%I:%M %p %d/%m/%y')]
    except Exception as e:
      times += [""]
  
  # Put everything together
  return [[t, p, r, l] for t, p, r, l in zip(times, problems, results, languages)]
