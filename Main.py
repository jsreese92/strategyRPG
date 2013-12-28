'''
Created on Dec 28, 2013

@author: jsreese
'''

from Environment import Tile
from Characters import *

def main():
  testTile = Tile.Tile(1,1,1,"grass")
  theStr = testTile.toString()
  print theStr
  
main()
  
