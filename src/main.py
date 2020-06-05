import settings
from automate import run_selenium
from scrape import start_scraping

def main():
  print("Starting up...")
  run_selenium()
  print("\u2713 Finished")

if __name__ == "__main__":
  main()