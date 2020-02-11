#!/bin/bash

cd crab_2017MC_3/
echo " "
echo $(pwd)

for i in */; 
do 
    echo " "
    echo " "
    echo " "
    echo "%%%%%%%%%%%%%%%%%%%"
    echo " "
    echo " "
    echo " "
    echo "### $i"; 
    #cd "$i/results"
    #echo "------" $(pwd)
    crab status $i
    #cd ../..
done;
