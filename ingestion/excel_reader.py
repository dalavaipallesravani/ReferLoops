import pandas as pd
import sys
sys.path.append("..")
from config import EXCEL_FILE_PATH

def read_excel_file(file_path=EXCEL_FILE_PATH):
    companies=[]
    df = pd.read_excel(file_path)
    for i,row in df.iterrows():
        #print(row["Company Name"], row["Careers URL"], row["Job Selector"], row["Next button selector"])
        company={
            "Company_name" : row["Company Name"],
            "Careers_URL" : row["Careers URL"],
            "Job_Selector" : row["Job Selector"],
            "Next_Button_Selector" : row["Next button selector"]
        }
        companies.append(company)
    return companies

if __name__ == "__main__":
    read_excel_file()
