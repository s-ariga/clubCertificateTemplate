from enum import Enum, auto


class Positions(Enum):
    AR60 = 0
    FR3X40 = 1
    FR60PR = 2
    AR60W = 3
    R3X40 = 4
    R60PR = 5
    AR60PR = 7
    AR40PR = 8
#    ARMIX = 9


'''
種目名
テンプレート読み込み前に、この中に無い種目名はエラーを返します

** Mix種目は射手数がちがうので別にする
** ARとSBを分けたのは気分
'''

ARM = ['AR60']
ARW = ['AR60W']
ARPR = ['AR60PR', 'AR40PR']
ARSH = ['R1', 'R4']
AR = ARM + ARW + ARPR + ARSH

SBM = ['FR3X20', 'FR60PR']
SBW = ['R3X20', 'R60PR']
SBSH = ['R6']
SB = SBM + SBW + SBSH

POSITIONS = SB + AR

MIX = ['ARMIX']  # ARMIXはPOSITIONSには入れない


def position_exists(name):
    '''
    種目名の文字列が存在するか調べて返す
    parameters
    name 種目名

    returns
    bool
    '''
    return True if name in POSITIONS else False
