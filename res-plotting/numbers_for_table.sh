#!/bin/bash
# This script will take a list of pulsars and produce 5 numbers for each of them
# minfreq
# maxfreq
# startMJD
# endMJD
# rms
# When I get my 5 numbers I need to get them in
# json, and then
# dump my json plane
# Web page from Shakeh that shows me how to:
# http://stackoverflow.com/questions/7100125/storing-python-dictionaries

# parse the list of pulsars, or if no list, then use all
# For now we are putting in a list of pulsars (this will need to change later - probably an input param)
declare -a pulsars=("J1853+1303" "J1455-3330" "B1953+29" "J0613-0200" "J1741+1351" "J1744-1134" "J1909-3744")

# For the list of pulsars do
for pulsar in "${pulsar[@]}" do
# find minfreq/maxfreq in each tim file
# Can I get AverageEpochs to do some of (all of) this?
# find startMJD/endMJD in each tim file
# run tempo2 on each and get the rms
# end do
done
