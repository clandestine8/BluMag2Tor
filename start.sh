#!/bin/bash

split -l 200 -d --additional-suffix=.ml.txt maglist.txt mags

shopt -s nullglob

c=0

tmux new -d -s 'm2t' 'while true; do ls *.torrent | wc -l; sleep 5; done'
for f in *.ml.txt
do
  tmux new -d -s "m2t$c" "python mag2tor2_py2.py '$f'"
  c=$((c+1))
done
