import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from excel_reader import read_excel_file
from utils import get_page
from selector_detector import detect_selectors
from datetime import datetime, timedelta
from config import MAX_AGE_DAYS, LOCATION_FILTER

def scrape_all_companies():
    companies=read_excel_file()
    all_jobs = []
    for company in companies:
        selectors = detect_selectors(company["Platform"])
        if selectors is None:
            print(f"No platform found for {company['Company_name']}. Skipping...")
            continue
        page, browser, playwright = get_page(company["Careers_URL"])
        
        while True:
            job_cards = page.query_selector_all(selectors["job_card_selector"])
            for card in job_cards:
                title = card.query_selector(selectors["job_title_selector"]).inner_text()
                #location = card.query_selector(selectors["location_selector"]).inner_text()
                #date  = card.query_selector(selectors["date_selector"]).inner_text()
                metadata = card.query_selector_all(selectors["metadata_selector"])
                location = metadata[0].inner_text() if len(metadata) > 0 else ""
                date = metadata[1].inner_text() if len(metadata) > 1 else ""
                job = {
                    "title": title,
                    "location": location,
                    "date": date,
                    "company": company["Company_name"],
                    "careers_URL": company["Careers_URL"]
                }
                if is_recent(date) and is_India(location):
                    all_jobs.append(job)
            if selectors["next_button_selector"] is None:
                break
            next_button = page.query_selector(selectors["next_button_selector"])
            if next_button and next_button.is_enabled():
                next_button.click()
                page.wait_for_timeout(2000)
            else:
                break
        browser.close()
        playwright.stop()    
    return all_jobs

def is_recent(date_str):
    date_str = date_str.replace("Updated:", "").strip()
    try:
        job_date = datetime.strptime(date_str, "%m/%d/%Y")
        return datetime.now() - job_date <= timedelta(days=MAX_AGE_DAYS)
    except:
        return False

def is_India(location_str):
    india_keywords = ["india", "ind", "bengaluru", "hyderabad", "mumbai", "delhi", "gurugram", "noida", "chennai", "pune"]
    return any(keyword in location_str.lower() for keyword in india_keywords)
        
if __name__ == "__main__":
    jobs = scrape_all_companies()
    print(f"Total jobs scraped: {len(jobs)}")
    for job in jobs:
        print(job)
