'''
Created on Dec 28, 2013

@author: jsreese
'''

class Tile:
  """This object contains information about an individual tile"""
  x = 0
  y = 0
  height=0
  landType="" # water, lava, etc.
  
  def __init__(self,theX,theY,theHeight,theType):
    self.x = theX
    self.y = theY
    self.height = theHeight
    self.landType = theType

  def toString(self):
    """Returns the string containing all a tile's parameters"""
    return 'x coordinate: %s, y coordinate: %s, height: %s, land type: %s.' % \
      (self.x, self.y, self.height, self.landType)


  def sameCoordinates(self,otherTile):
    """Boolean, returns true if tiles have same x and y coordinates"""
    thisX = self.x
    thisY = self.y
    otherX = otherTile.x
    otherY = otherTile.y

    if((thisX == otherX) and (thisY == otherY)):
      return False
    else: 
      return True

  def equals(self,otherTile):
    """Returns true if self has exact same variables as otherTile"""
    thisX = self.x
    thisY = self.y
    thisHeight = self.height
    thisType = self.landType
    otherX = otherTile.x
    otherY = otherTile.y
    otherHeight = otherTile.height
    otherType = otherTile.landType
    
    if((thisX == otherX) and (thisY == otherY) and (thisHeight == otherHeight)
        and (thisType == otherType)):
      return True
    else:
      return False
