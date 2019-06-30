#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
import datetime
import argparse

import jinja2
import pandas as pd

import ParseCertificateTemplate as tp
import Positions as pos

# テンプレート置き場
TEMPLATE_DIR = "../template/"
TEMPLATE_INDIVIDUAL = "certificate-indivi.html"
TEMPLATE_MIXTEAM = "certificate-mixteam.html"
TEMPLATE_TEAM_POSI = "certificate-tem-posi.html"
TEMPLATE_TEAM_COMBI = "certificate-team-combi.html"

# 成績置き場
RESULT_DIR = "../results/"
RESULT_INDIVIDUAL = RESULT_DIR + "individual.xlsx"
RESULT_MIXTEAM = RESULT_DIR + "mixteam.xlsx"
RESULT_TEAM_POSI = RESULT_DIR + "team_posi.xlsx"
RESULT_TEAM_COMBI = RESULT_DIR + "team_combi.xlsx"

# 出力先
OUTPUT_DIR = "../output/"
OUTPUT_TEAM_COMBI = OUTPUT_DIR+"teamCombined{0}.html"

def createCerts():
    pass

def createCertsTeamCombined():

    result = pd.read_excel(RESULT_TEAM_COMBI)
    
    html = tp.ParseCertificateTemplate(TEMPLATE_DIR, TEMPLATE_TEAM_COMBI, result)

    rank = 1
    for cert  in html.getCertificate():
        with open(OUTPUT_TEAM_COMBI.format(str(rank)), mode="w", encoding='utf-8') as f:
            f.write(cert)
        rank += 1
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'クラブ戦用の賞状をhtmlで作成する')
    parser.add_argument('--position', '-p', nargs='*',
                        help='作成する種目')
    parser.add_argument('--team', '-t', action='store_true',
                        help='種目別団体の表彰状を作成')
    parser.add_argument('--all', '-a', action='store_true',
                        help='全種目の表彰状を作成')
    parser.add_argument('--combined', '-c', action='store_true',
                        help='総合団体の表彰状を作成')
    parser.add_argument('--version', '-v', action='version',
                        version=os.path.basename(__file__) + ' ver.0.1')
    args = parser.parse_args()

    
    if args.combined:
        createCertsTeamCombined()
    
