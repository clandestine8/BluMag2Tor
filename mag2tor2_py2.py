#!/usr/bin/env python
#
# Inspired by the Magnet2Torrent script from the
# https://github.com/danfolkes/Magnet2Torrent.git

import libtorrent
import time
import sys
import os.path
import argparse
import urlparse


def mag2tor(mag_link, count):
    parsed = urlparse.urlparse(mag_link)
    sys.stdout.write("[{}]".format(count))
    sys.stdout.flush()
    if not os.path.isfile(urlparse.parse_qs(parsed.query)['dn'][0]):
        sys.stdout.write(' Progress: ')
        sess = libtorrent.session()
        prms = {
            'save_path': os.path.abspath(os.path.curdir),
            'paused': False,
            'auto_managed': False,
            'upload_mode': True,
        }
        torr = libtorrent.add_magnet_uri(sess, mag_link, prms)
        dots = 0
        while (not torr.has_metadata() and dots != 20):
            dots += 1
            sys.stdout.write('=')
            sys.stdout.flush()
            time.sleep(1)
        if (dots): sys.stdout.write(' ')
        sess.pause()
        if (dots != 20):
            sys.stdout.write(urlparse.parse_qs(parsed.query)['dn'][0] + ' Success!')
            sys.stdout.write('\n')
            tinf = torr.get_torrent_info()
            f = open(urlparse.parse_qs(parsed.query)['dn'][0], 'wb')
            f.write(libtorrent.bencode(
                libtorrent.create_torrent(tinf).generate()))
            f.close()
        else:
            sys.stdout.write(urlparse.parse_qs(parsed.query)['dn'][0] + ' Failed & Skipped!')
            sys.stdout.write('\n')
        sess.remove_torrent(torr)
    else:
        sys.stdout.write(' Already Completed! \n')
        sys.stdout.flush()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file with list of magnet links")
    args = parser.parse_args()
    while True:
        count = 0
        with open(args.file, "r") as f:
            lines = f.read().splitlines()
            for line in lines:
                count += 1
                mag2tor(line, count)
