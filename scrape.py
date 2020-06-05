import csv
from datetime import datetime
from enum import Enum
import os
from bs4 import BeautifulSoup

def write_to_csv(submissions):
  with open('output/data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Time', 'Problem', 'Result', 'Language'])
    for submission in submissions:
      writer.writerow(submission)

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
    
    # Put everything together
    submissions += [[t, p, r, l] for t, p, r, l in zip(times, problems, results, languages)]

  # Sort and write to csv
  submissions.sort(reverse=True)
  write_to_csv(submissions)
