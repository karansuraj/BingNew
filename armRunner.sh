#!/bin/bash
VAR=$0
DIR=$(dirname "$VAR")
cd "$DIR"
echo Ran now
python3.5 brewardsPort.py -h