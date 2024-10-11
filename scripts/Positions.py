from enum import Enum


class Positions(Enum):
    ARM = 0
    R3PM = 1
    RPRM = 2
    ARW = 3
    R3PW = 4
    RPRW = 5
    ARPR = 7
    AR40PR = 8
    ARMIX = 9
    FR3X20BR = 10
    FR60PRBR = 11
    FR40PRBR = 12
    FR20PRBR = 13


'''
種目名
テンプレート読み込み前に、この中に無い種目名はエラーを返します

** Mix種目は射手数がちがうので別にする
** ARとSBを分けたのは気分
'''

ARM = ['ARM']
ARW = ['ARW']
ARPR = ['ARPR']
ARSH = ['R1', 'R4']
AR = ARM + ARW + ARPR + ARSH

SBM = ['R3PM', 'RPRM']
SBW = ['R3PW', 'RPRW']
SBSH = ['R6']
SB = SBM + SBW + SBSH

P300 = ['FR60PR', 'FR3X20', 'FR40PR', 'FR20PR']

POSITIONS = SB + AR + P300

ARMIX = ['ARMIX']  # ARMIXはPOSITIONSには入れない
POSITIONS = POSITIONS + ARMIX


def position_exists(name):
    '''
    種目名の文字列が存在するか調べて返す
    parameters
    name 種目名

    returns
    bool
    '''
    return True if name in POSITIONS else False
