from enum import Enum, auto

class Positions(Enum):
    AR60 = 0
    FR3X40 = 1
    FR60PR = 2
    AR60W = 3
    R3X40 = 4
    R60PR = 5
    AR60PR = 7
#    ARMIX = 6

AR = ['AR60',
      'AR60W',
      'AR60PR']

MIX = ['ARMIX']

SB = ['FR3X40',
      'FR60PR',
      'R3X40',
      'R60PR']

POSITIONS = AR + SB + MIX

def position_exists(name):
    '''
    種目名の文字列が存在するか調べて返す
    parameters 
    name 種目名

    returns
    bool
    '''
    assert name in POSITIONS, 'Wrong position name: ' + name 
    return True if name in POSITIONS else False
