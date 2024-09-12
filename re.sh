#!/bin/bash

folder=$(basename "$PWD")
cd ../
sudo rm -r $folder
git clone https://github.com/patrickwuva/api-dev.git
cd $folder