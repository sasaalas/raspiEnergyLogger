#!/bin/sh
#
# @(#)$Id$
#
# Purpose
cp /your/path/to/raspiEnergyLogger/efergyLogger/efergyLog.txt /your/path/to/raspiEnergyLogger/efergyParser/
python3 /your/path/to/raspiEnergyLogger/efergyParser/efergyParser.py --url 192.168.0.2 --dataFile /your/path/to/raspiEnergyLogger/efergyParser/efergyLog.txt --brokerUrl 192.168.0.2 --brokerPort 1883
truncate -s 0 /your/path/to/raspiEnergyLogger/efergyLogger/efergyLog.txt
