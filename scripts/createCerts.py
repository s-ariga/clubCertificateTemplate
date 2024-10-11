#!/usr/bin/env python
# -*- coding : utf-8 -*-
# Seiichi Ariga <seiichi.ariga@gmail.com>

import os
import sys
import argparse
import pandas as pd

import ParseCertificateTemplate as tp
import Positions as pos

# import ClubConfig

# テンプレート置き場ディレクトリ
TEMPLATE_DIR = "../template/"
# テンプレートファイル名
TEMPLATE_INDIVIDUAL = "certificate-indivi.html"
TEMPLATE_MIXTEAM = "certificate-mixteam.html"
TEMPLATE_TEAM_POSI = "certificate-team-posi.html"
TEMPLATE_TEAM_COMBI = "certificate-team-combi.html"
TEMPLATE_ARPR = "certificate-arpr.html"  # ARPRは大会の回数が違う
TEMPLATE_TEAM_ARPR = "certificate-team-arpr.html"

# 成績置き場ディレクトリ
RESULT_DIR = "../results/"
# 成績ファイル名
RESULT_INDIVIDUAL = RESULT_DIR + "individual.xlsx"
RESULT_MIXTEAM = RESULT_DIR + "mixteam.xlsx"
RESULT_TEAM_POSI = RESULT_DIR + "team_position.xlsx"
RESULT_TEAM_COMBI = RESULT_DIR + "team_combi.xlsx"

# 出力先ディレクトリ
OUTPUT_DIR = "../output/"
# 出力ファイル名
OUTPUT_INDIVIDUAL = OUTPUT_DIR + "Individual{0}-{1}.html"
OUTPUT_MIXTEAM = OUTPUT_DIR + "MixTeam{0}-{1}.html"
OUTPUT_TEAM_POSITION = OUTPUT_DIR + "Team{0}-{1}.html"
OUTPUT_TEAM_COMBI = OUTPUT_DIR + "TeamCombined{0}-{1}.html"


def createCerts(positions, result_file, template_file, output_file, team=False):
    html = {}
    cert_html = {}
    for posi in positions:
        if pos.position_exists(posi):
            print(result_file, "ファイル名:", posi)
            result = pd.read_excel(result_file, sheet_name=posi)
            html[pos] = tp.ParseCertificateTemplate(TEMPLATE_DIR,
                                                    template_file,
                                                    result)
            cert_html[pos] = html[pos].getCertificate(position=posi, team=team)
            outputHTML(cert_html[pos], output_file, posi)
        else:
            print("Position " + posi + " doesn't exist.")
    return cert_html


def createCertsIndividual(positions):
    '''
    個人種目の表彰状を作成
    '''

    html = {}
    cert_html = createCerts(positions, RESULT_INDIVIDUAL, TEMPLATE_INDIVIDUAL,
                            OUTPUT_INDIVIDUAL)


def createCertsTeam(positions):
    '''
    種目別団体の表彰状を作成
    '''

    html = {}
    cert_html = {}
    for posi in positions:
        result = pd.read_excel(RESULT_TEAM_POSI, sheet_name=posi)
        html[posi] = tp.ParseCertificateTemplate(TEMPLATE_DIR,
                                                TEMPLATE_TEAM_POSI,
                                                result)
        cert_html[posi] = html[posi].getCertificate(position=posi, team=True)
        outputHTML(cert_html[posi], OUTPUT_TEAM_POSITION, posi)


def createCertsMixTeam():
    '''
    ミックスチームの表彰状を作成
    ミックスチームは、射手が二人なので、別テンプレート
    '''
    result = pd.read_excel(RESULT_MIXTEAM)
    html = tp.ParseCertificateTemplate(TEMPLATE_DIR,
                                       TEMPLATE_MIXTEAM,
                                       result)
    cert_html = html.getCertificate(position='ARMIX')
    outputHTML(cert_html, OUTPUT_MIXTEAM)


def createCertsTeamCombined():
    '''
    総合団体の賞状を作成する
    '''
    result = pd.read_excel(RESULT_TEAM_COMBI)
    html = tp.ParseCertificateTemplate(TEMPLATE_DIR,
                                       TEMPLATE_TEAM_COMBI,
                                       result)
    cert_html = html.getCertificate()
    outputHTML(cert_html, OUTPUT_TEAM_COMBI)


def outputHTML(html, filename, posi=''):
    '''
    HTMLをファイル出力
    '''
    # assert isinstance(posi, str), '種目名指定エラー'
    rank = 1
    for cert in html:
        assert rank < 9, '順位が9位以上あります'
        print(filename)
        with open(filename.format(posi, str(rank)),
                  mode='w', encoding='utf-8') as f:
            f.write(cert)
        rank += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='クラブ戦用の賞状をhtmlで作成する')
    parser.add_argument('--position', '-p', nargs='*',
                        help='作成する種目')
    parser.add_argument('--team', '-t', action='store_true',
                        help='種目別団体の表彰状を作成')
    parser.add_argument('--mixteam', '-m', action='store_true',
                        help='ミックスチームの表彰状を作成')
    parser.add_argument('--all_positions', '-a', action='store_true',
                        help='全種目の表彰状を作成.総合団体ミックスチーム以外')
    parser.add_argument('--combined', '-c', action='store_true',
                        help='総合団体の表彰状を作成')
    parser.add_argument('--version', '-v', action='version',
                        version=os.path.basename(__file__) + ' ver.0.1.10')
    args = parser.parse_args()

    if args.position:
        for p in args.position:
            if not pos.position_exists(p):
                print('不正な種目名 "' + p + '" です. 種目名は以下のどれか')
                print(pos.POSITIONS)
                assert False, '種目名エラー'
                sys.exit('Position name Error.')
            if p == 'AR60PR':  # AR40は廃止(2022)
                createCerts(pos.ARPR, RESULT_INDIVIDUAL,
                            TEMPLATE_ARPR, OUTPUT_INDIVIDUAL)
            else:
                createCertsIndividual(args.position)
        if args.team:
            # !AR60PRとAR40PRは別の試合扱い
            # AR60PRは試合名が違うので、別のテンプレートを使用
            if 'ARPR' in args.position:  # !AR40PRは2022年から廃止
                createCertsTeam('AR60PR')
                # createCerts(pos.ARPR, RESULT_TEAM_POSI,
                #           TEMPLATE_TEAM_ARPR, OUTPUT_TEAM_POSITION)
            else:
                createCertsTeam(args.position)
    if args.mixteam:
      # ミックスチームは2人組なので専用テンプレートを使用
        createCertsMixTeam()
    if args.all_positions:
        createCertsIndividual(pos.POSITIONS)
        createCerts(pos.ARPR, RESULT_INDIVIDUAL,
                    TEMPLATE_ARPR, OUTPUT_INDIVIDUAL)
        if args.team:
            createCertsTeam(pos.POSITIONS)
            createCerts(pos.ARPR,
                        RESULT_INDIVIDUAL,
                        TEMPLATE_TEAM_ARPR,
                        OUTPUT_TEAM_POSITION,
                        team=True)
    if args.combined:
        createCertsTeamCombined()
