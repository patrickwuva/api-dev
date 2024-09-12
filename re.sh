#!/bin/bash

folder=$(basename "$PWD")
cd ../
sudo rm -r $folder
git clone https://patrickwuva/api-dev.tmp
cd $folder