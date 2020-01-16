#!/usr/bin/env python
#

import argparse
import urllib.parse as urlparse
from urllib.parse import parse_qs

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", help="file successful torrents")
    parser.add_argument("file2", help="file with list of magnet links")
    args = parser.parse_args()
    
    G = open(args.file1, "r")
    M = open(args.file2, "r")
    
    G = G.read().splitlines()
    Mlines = M.read().splitlines()
    F = open('outputlist.txt', 'w')
    for m in Mlines:
        mp = urlparse.urlparse(m)
        fn = urlparse.parse_qs(mp.query)['dn'][0]
        
        if not fn in G:
            F.write(m + "\n")
    F.close()
