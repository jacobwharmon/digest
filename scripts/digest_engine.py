import os
import sys
#import argparse # new data collection Y/N

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append('dir_path')

from gather import *
from prepare import *
from send import *

if __name__ == '__main__':
    # GATHER DIGEST MATERIALS
    quote_clean = gather_quote()
    headlines_clean = gather_headlines()
    series_clean = gather_series()

    # PREPARE THE DIGEST
    pdf_clean = prepare_pdf(quote_clean, headlines_clean, series_clean)

    # SEND DIGEST
    send_email(pdf_clean)
    