import settings
from automate import run_selenium
from scrape import start_scraping

def main():
  run_selenium()
  start_scraping()

if __name__ == "__main__":
  main()