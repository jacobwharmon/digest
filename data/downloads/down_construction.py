import urllib.request
from urllib.error import HTTPError
import os

current_url = "https://www.census.gov/construction/c30/xls/totsa.xls"
construction_path = "data/raw/construction"

historic_urls = []
historic_filenames = []
for year in range(2004,2017):
    for month in range(1,13):
        historic_urls.append(f"https://www.census.gov/construction/c30/xls/pr{year}{month:02d}.xls")
        historic_filenames.append(f"{year}{month:02d}.xls")
for year in range(2017,2022):
    for month in range(1,13):
        historic_urls.append(f"https://www.census.gov/construction/c30/xls/pr{year}{month:02d}.xlsx")
        historic_filenames.append(f"{year}{month:02d}.xlsx")

historic_dict = dict(zip(historic_filenames, historic_urls))
historic_dict.pop('201309.xls')

def down_construction():
    """Collects the Value of Construction Put in Place Survey (VIP) monthly estimates of the total dollar value of construction work done in the U.S.
    
    URL: https://www.census.gov/construction/c30/prexcel.html
    """
    # Downloads historic datasets if not already downloaded
    for hist_name, hist_url in historic_dict.items():
        if hist_name not in os.listdir(construction_path):
            try:
                urllib.request.urlretrieve(hist_url, f"{construction_path}/{hist_name}")
            except HTTPError:
                print("No more months to download\n")
            
            # Download most recent dataset as well
            urllib.request.urlretrieve(current_url, f"{construction_path}/totsa.xls")
    

