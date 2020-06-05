import csv
import os
from time import sleep
from scrape import start_scraping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def write_to_csv(submissions):
  with open('output/data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Time', 'Problem', 'Result', 'Language'])
    for submission in submissions:
      writer.writerow(submission)


def run_selenium():
  # Store all submission data after scraping
  submissions = [] 

  # Add options for running headless(without window)
  chrome_options = Options()
  chrome_options.add_argument('--headless')

  driver = webdriver.Chrome(options=chrome_options)
  driver.get(f"https://www.codechef.com/users/{os.getenv('USERNAME')}")
  
  # Wait 1s for page to load
  sleep(1)
  try:
    for num in range(1, 100):
      submissions += start_scraping(driver.page_source)
      
      # Check if next button is still there
      # Otherwise it will never terminal
      driver.find_element_by_xpath("//img[contains(@src,'/sites/all/themes/abessive/images/page-next-active.gif')]")
      
      # Run js for going to next page
      driver.execute_script("onload_getpage_recent_activity_user('next');")
      
      # Wait 1s for page to load
      sleep(1)
  except Exception as error:
    driver.close()
    write_to_csv(sorted(submissions))