#!/usr/bin/env python
# -*- coding : utf-8 -*-

import os
import sys
import datetime
import argparse
import jinja2
import pandas as pd

import ParseCertificateTemplate as tp
import Positions as pos

from ClubConfig import *


def createCerts(positions, result_file, template_file, output_file, team=False):
    html = {}
    cert_html = {}
    for posi in positions:
        if pos.position_exists(posi):
            print(result_file)
            result = pd.read_excel(result_file, sheet_name=posi)
            html[pos] = tp.ParseCertificateTemplate(TEMPLATE_DIR,
                                                    template_file,
                                                    result)
            cert_html[pos] = html[pos].getCertificate(position=posi, team=team)
            outputHTML(cert_html[pos], output_file, posi)
        else:
            print("Position " + posi + "doesn't exist.")
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
    for pos in positions:
        result = pd.read_excel(RESULT_TEAM_POSI, sheet_name=pos)
        html[pos] = tp.ParseCertificateTemplate(TEMPLATE_DIR,
                                                TEMPLATE_TEAM_POSI,
                                                result)
        cert_html[pos] = html[pos].getCertificate(position=pos, team=True)
        outputHTML(cert_html[pos], OUTPUT_TEAM_POSITION, pos)


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


def outputHTML(html, filename, pos=''):
    '''
    HTMLをファイル出力
    '''
    assert type(pos) is str, '種目名指定エラー'
    rank = 1
    for cert in html:
        assert rank < 9, '順位が9位以上あります'
        with open(filename.format(pos, str(rank)),
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
                        version=os.path.basename(__file__) + ' ver.0.1')
    args = parser.parse_args()

    if args.position:
        for p in args.position:
            if not pos.position_exists(p):
                print('不正な種目名です. 種目名は以下のどれか')
                print(pos.POSITIONS)
                assert False, '種目名エラー'
                sys.exit('Position name Error.')
            if p == 'AR60PR' or p == 'AR40PR':
                createCerts(pos.ARPR, RESULT_INDIVIDUAL,
                            TEMPLATE_ARPR, OUTPUT_INDIVIDUAL)
            else:
                createCertsIndividual(args.position)
        if args.team:
            # AR60PRとAR40PRは別の試合扱い
            if 'AR60PR' in args.position or 'AR40PR' in args.position:
                createCerts(pos.ARPR, RESULT_TEAM,
                            TEMPLATE_ARPR_TEAM, OUTPUT_TEAM_POSITION)
            else:
                createCertsTeam(args.position)
    if args.mixteam:
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
