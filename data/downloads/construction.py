import urllib.request

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

def down_construction(historic=False):
    """Collects the Value of Construction Put in Place Survey (VIP) monthly estimates of the total dollar value of construction work done in the U.S.
    URL: https://www.census.gov/construction/

    Args:
        historic (bool, optional): Determines if we need to collect historic datasets as well. Defaults to False.
    """
    if historic:
        # Download historic and current
        # HTTP 429 Too many requests error 
        # Needs to not repeat old downloads. for file in dir, ignore
        [urllib.request.urlretrieve(hist_url, f"{construction_path}/{hist_name}") for hist_name, hist_url in historic_dict.items()]
        urllib.request.urlretrieve(current_url, f"{construction_path}/totsa.xls")
    else:
        # Download current
        urllib.request.urlretrieve(current_url, f"{construction_path}/totsa.xls")
    
