import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def run_selenium():
  # Add options for running headless(without window)
  print("Starting up......")
  chrome_options = Options()
  chrome_options.add_argument('--headless')

  # options=chrome_options
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(f"https://www.codechef.com/users/{os.getenv('USERNAME')}")
  sleep(1)

  print(f"On {os.getenv('USERNAME')} profile page")

  try:
    for num in range(1, 10**9):
      with open(f'codechef/page_{num}.html', 'w') as html_file:
        html_file.write(driver.page_source)
        print(f"Page {num} saved..")
      
      driver.find_element_by_xpath("//img[contains(@src,'/sites/all/themes/abessive/images/page-next-active.gif')]")
      driver.execute_script("onload_getpage_recent_activity_user('next');")
      print("On next page")
      sleep(1)
  except Exception as error:
    driver.close()
    print('Finished...')