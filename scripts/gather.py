from asyncio.windows_events import NULL
import os
import requests

def gather_quote():
    """Pings Quotable's random quote API and returns the quote body and author

    Returns:
        quote_clean: a single string containing the quote and author
    """
    
    api = "https://api.quotable.io/random"
    quote_json = requests.get(api).json()
    quote_clean = f"{quote_json['content']} --{quote_json['author']}"
    return quote_clean

def gather_headlines():
    """[summary]

    Returns:
        [type]: [description]
    """
    headlines_clean = NULL
    return headlines_clean

def gather_series():
    """[summary]

    Returns:
        [type]: [description]
    """
    series_clean = NULL
    return series_clean
