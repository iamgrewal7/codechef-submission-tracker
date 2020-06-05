from bs4 import BeautifulSoup
from enum import Enum
import os
from texttable import Texttable
from datetime import datetime

# class Results(Enum):
#   WA = 1
#   AC = 2
#   TLE = 3
#   PA = 4
#   CE = 5
#   RE = 6

# RESULT_MAP = {
#   'wrong answer': Results.WA,
#   'time limit exceeded': Results.TLE,
# }

def start_scraping():
  submissions = []
  for page in os.listdir('codechef/'):
    with open(f"codechef/{page}") as fp:
        soup = BeautifulSoup(fp, "lxml")

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
      times += [datetime.strptime(all_tds[i].contents[0], '%I:%M %p %d/%m/%y')]

    submissions += [[t, p, r, l] for t, p, r, l in zip(times, problems, results, languages)]

  submissions.sort(reverse=True)
  table = Texttable()
  table.add_row(['Time', 'Problem', 'Result','Language'])
  for t, p, r, l in submissions:
    table.add_row([t, p, r, l])
  print(table.draw())
