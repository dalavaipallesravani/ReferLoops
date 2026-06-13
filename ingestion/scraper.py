#import requests
#from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from excel_reader import read_excel_file

def sample_requests():
    #response = requests.get('https://www.amazon.jobs/content/en/teams/international-stores/india')
    companies=read_excel_file()
    #URL = 'https://www.amazon.jobs/content/en/teams/international-stores/india'

    for company in companies:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(company["Careers_URL"])
            page.wait_for_timeout(3000)
            all_jobs=[]
            while True:
                jobs=page.query_selector_all(company["Job_Selector"])
                for job in jobs:
                    all_jobs.append(job.inner_text())
                next_button=page.query_selector(company["Next_Button_Selector"])
                if next_button:
                    next_button.click()
                    page.wait_for_timeout(3000)
                else:
                    break          
            if len(all_jobs)==0:
                print(f"Warning: Selector may be broken for{company['Company_name']}")
            else:
                print(f"{company['Company_name']} : {len(all_jobs)} jobs found")

if __name__ == "__main__":
    sample_requests()
