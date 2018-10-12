#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------
# Packages needed
# Matplotlib
# Python3
# PyQt5
#
#------------------------------------------------------------
#
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
#------------------------------------------------------------

from pprint import pprint
from yahoo_finance import Share

yahoo = Share('YHOO')
print(yahoo.get_open())

print(yahoo.get_price())

#pprint(yahoo.get_historical('2017-01-01', '2018-01-01'))