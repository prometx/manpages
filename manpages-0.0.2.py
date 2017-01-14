#!/usr/bin/env python

"""

This is an attempt to create a simple tool to locate and represent
GNU/Linux man pages in a simple gui interface, i.e., a "manpage bible"

"""


import io
import sys
import subprocess
from pathlib import Path


__author__ = "Allen L. Rees II"
__copyright__ = "Copyright 2017, Shiva Heavy Industries"
__credits__ = ["Wakantanka", "Moms", "Fate & Whimsy", "The Tao"]
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Allen Rees"
__email__ = "prometx@gmail.com"
__status__ = "Mad Alpha yo..."

#
#an attempt to "stat" the popular Linux manpage directories
#

print (' ' + '\n')

locPath = subprocess.Popen('manpath', shell=True)

print (' ' + '\n')

subprocess.call('ls')

print (' ' + '\n')

print (locPath)


sys.exit()




