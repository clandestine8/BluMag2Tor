# BluMag2Tor
Make Torrents from Accessible Magnet Links Using Libtorrent
### Setup Requirements:
- Python 2.7 OR Python 3
- libtorrent compatible with you Python Version
- List of Magnet Links Including:
  - InfoHash
  - Tracker (`tr=https://mytrack.com/announce/randompasskey`)
  - Torrent File Name (`dn=1234abcd.torrent` Note: include the .torrent here)
  - Save List as `maglist.txt`
- `tmux` must be installed


### How to Run
- Make a folder and place `mag2tor2.py` [Python 3] OR `mag2tor2_py2.py` [Python 2.7] along with start.sh and maglist.txt
- Open `start.sh` in nano or your favorite text editor 
- find line `split -l 200 -d --additional-suffix=.ml.txt maglist.txt mags` 
- Edit `-l 200` to you liking. 
  - **NOTE:** This will split your list into lists of 200 by default - if the master list has 1000 links then it will create 5 instances of mag2tor2.py looping through each list of 200
  - If you want More Instances then reduce the number, if you want less increase the number
  - If you list is less than 200 Leave as it is
- Run `./start.sh` from with the folder

After a few moments it will begin creating torrent files from resolved magnet links, if it fails to resolve the metadata from the swarm it will fail after 90 seconds and move on to the next line
It will loop indefinately, even if all torrents are resolved

You can monitor by running `tmux attach -t m2t` - this will give you a running count of torrent files created in the folder. 
You can view each instances output by navigating through the various tmux screens (ie. `CTRL+B`, `W`)



Extended From & Inspired by https://github.com/xrgtn/mag2tor which its self was inspired by https://github.com/danfolkes/Magnet2Torrent
