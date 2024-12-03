#!/bin/bash

# Build the project

pwd
cd buildfiles
pwd
cd $(ls -d */ | head -n 1)  # Change into the next folder
pwd
echo "Building the project"
make
cp YOUR-OUTPUT-LOCATION ../../outputs/OUTFILENAME
exit 0