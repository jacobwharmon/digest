import os
import sys
#import argparse # new data collection Y/N

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append('dir_path')

from construction import *

if __name__ == '__main__':
    down_construction()