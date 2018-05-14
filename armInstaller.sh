#!/bin/bash
tar -xf dependencies/geckodriver-v0.11.1-arm7hf.tar.gz
sudo mv geckodriver /usr/bin
sudo apt-get install xvfb
sudo pip install pyvirtualdisplay
sudo pip install selenium