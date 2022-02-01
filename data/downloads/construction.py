import urllib.request

current_url = "https://www.census.gov/construction/c30/xls/totsa.xls"
construction_path = "data/construction"

def down_construction(historic=False):
    """Collects the Value of Construction Put in Place Survey (VIP) monthly estimates of the total dollar value of construction work done in the U.S.
    URL: https://www.census.gov/construction/

    Args:
        historic (bool, optional): Determines if we need to collect historic datasets as well. Defaults to False.
    """
    # Download current
    urllib.request.urlretrieve(current_url, f"{construction_path}/totsa.xls")
    
    # Download historic
    if historic:
        print('historic')
    else:
        pass
    
