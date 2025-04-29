#!/bin/bash
source .venv/bin/activate
python StatsFetcher.py 15 > time15.txt
sleep 8
python StatsFetcher.py 60 > time60.txt
