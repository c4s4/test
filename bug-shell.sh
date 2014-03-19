#!/bin/sh
# 
# This script demonstrates a funny shell bug.

mkdir -p ~/toto/tata/titi
cd ~/toto/tata/titi
rm -rf ~/toto
pwd
cd ..
pwd

