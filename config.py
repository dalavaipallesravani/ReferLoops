#File paths
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE_PATH = os.path.join(BASE_DIR, "companies.xlsx")

#Scraping hyper parameters
MAX_AGE_DAYS = 4
SCRAPE_INTERVAL_HOURS = 24
LOCATION_FILTER = "India"

#Matching hyper parameters
TOP_N = 10

# Excel column names
COL_COMPANY_NAME = "Company Name"
COL_CAREER_URL = "Careers URL"
COL_PLATFORM = "Platform"

