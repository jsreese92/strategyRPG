'''
Created on Dec 28, 2013

@author: jsreese

'''

from Environment import *

class Map:
  """This object contains width * length objects of type Tile"""
  width=0
  length=0
  tileList=[]
  
  # requires list of tiles of size theWidth*theLength
  def __init__(self,theWidth,theLength,theList):
    self.width = theWidth
    self.length = theLength
    self.tileList = theList

    listLen = len(theList)
    numTiles = theWidth*theLength
    if(listLen == numTiles):
      # make sure no two tiles have the same x and y coordinates
      for tile in theList:
        numSame = 0
        for otherTile in theList:
          if(tile.sameCoordinates(otherTile)):
            numSame+=1
        if(numSame > 1): # if more than one have same coordinates, error
          print("ERROR: Tiles exist with overlapping x and y coordinates")
    else:
      print "ERROR: Wrong number of tiles for this map"

