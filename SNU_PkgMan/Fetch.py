# Start of script
''' Fetch.py
Fetch SNU packages from the SNU Repositories
License: GNU General Public License V3.0 (GPL3)
Note: this script is highly incomplete. It currently serves as a reference for how the package manager will fetch and aggregate packages. It may not be functional at the moment. It has not yet been tested.
'''
# Import section
import os
import pygui
# Functions section
def dimensionalFetch():
  fetch('https://github.com/seanpm2001/SNU_0D/README.md') # Fetches SNU 0D mode packages
  fetch('https://github.com/seanpm2001/SNU_1D/README.md') # Fetches SNU 1D mode packages
  fetch('https://github.com/seanpm2001/SNU_2D/README.md') # Fetches SNU 2D mode packages
  fetch('https://github.com/seanpm2001/SNU_3D/README.md') # Fetches SNU 3D mode packages
  fetch('https://github.com/seanpm2001/SNU_4D/README.md') # Fetches SNU 4D mode packages
  break
def interface():
  # Coming soon
  break
def aggregatePackages():
  # Coming soon
  break
def main():
  return dimensionalFetch() as aggregatePackages()
  return interface()
  break
# Main section
return main()
break
""" File info
File type: Python source file (*.py)
File version: 1 (2022, Wednesday, May 4th at 7:56 pm PST)
Line count (including blank lines and compiler line): 37
"""
# End of script
