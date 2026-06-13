import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PLATFORM_SELECTORS = {
    "icims": {
    "job_card_selector": "div.job-card-module_root__QYXVA",
    "job_title_selector": "a.header-module_title__9-W3R",
    #"location_selector": "div.metadatum-module_text__ncKFr:first-of-type",
    #"date_selector": "div.metadatum-module_text__ncKFr:last-of-type",
    "metadata_selector": "div.metadatum-module_text__ncKFr",
    "next_button_selector": "button[data-test-id='next-page']"
},
    "turbohire": {
    "job_card_selector": "div[stroke='#EBEFFF']",
    "job_title_selector": "span.MuiLink-root-519",
    "metadata_selector": "span.MuiTypography-caption-156",
    "date_selector": "span.MuiTypography-overline-166",
    "next_button_selector": None
}
}
def detect_selectors(platform):
    return PLATFORM_SELECTORS.get(platform, None)

if __name__ == '__main__':
    result = detect_selectors("icims")
    print(result)