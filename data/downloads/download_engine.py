import os
import sys
#import argparse # new data collection Y/N

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append('dir_path')

from down_construction import *

if __name__ == '__main__':
    down_construction()
    # down_indexes()
    # down_housing_indexes()