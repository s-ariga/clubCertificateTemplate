#!/usr/bin/env python
# -*- coding : utf-8 -*-

'''
クラブ戦用
賞状テンプレートを読んで、htmlとして返す
'''
import os
import jinja2
import pandas as pd
import datetime

import Positions as posi

POSI = 'Position'
SCORE = 'Score'
RANK = 'Rank'
TEAM = 'Team'
NAME = 'Name'
NAME1 = 'Name1'
NAME2 = 'Name2'
NAME3 = 'Name3'

CERT_RANKS = 6

class ParseCertificateTemplate():
    def __init__(self, path, filename, data):
        '''
        初期化でjinja2のインスタンスを作る
        
        parameters
        path : テンプレートの相対パス str
        filename : テンプレートのファイル名 str
        data : 成績 DataFrame
        '''
        self.tmplt_loader = jinja2.FileSystemLoader(searchpath=path)
        self.tmplt_env = jinja2.Environment(loader=self.tmplt_loader)
        self.tmplt_file = filename
        assert os.path.exists(path + filename), 'テンプレートファイルが存在しない'
        self.df = data
        assert len(self.df) == CERT_RANKS, '表彰者数が6じゃない'

        today = datetime.date.today()
        self.year = self.get_reiwa(today.year, gannen = True)
        self.month, self.day = today.month, today.day

    def getCertificate(self, position='', team=False):
        '''
        テンプレートに成績を流し込み、順位順にhtmlのリストに入れて返す

        parameters
        position : 種目名 デフォルト=団体
        team : 種目別団体 デフォルト=種目別個人

        returns
        html : データを流し込んだテンプレート
        '''
        assert type(position) is str, '種目名指定エラー'
        assert self.tmplt_file is not None, 'Class not properly initialized.'
        template = self.tmplt_env.get_template(self.tmplt_file)

        html = []
        for index, item in self.df.iterrows():
            if position in posi.AR+posi.SB:
                if team == True:
                    output = template.render(position = item[POSI],
                                             score = item[SCORE],
                                             rank = item[RANK],
                                             team = item[TEAM],
                                             name1 = item[NAME1],
                                             name2 = item[NAME2],
                                             name3 = item[NAME3],
                                             year = self.year,
                                             month = self.month,
                                             day = self.day)
                else:
                    output = template.render(position = item[POSI],
                                             score = item[SCORE],
                                             rank = item[RANK],
                                             team = item[TEAM],
                                             name = item[NAME],
                                             year = self.year,
                                             month = self.month,
                                             day = self.day)
            elif position == posi.MIX:
                output = template.render(score = item[SCORE],
                                         rank = item[RANK],
                                         team = item[TEAM],
                                         name1 = item[NAME1],
                                         name2 = item[NAME2],
                                         year = self.year,
                                         month = self.month,
                                         day = self.day)
            else:
                output = template.render(score = item[SCORE],
                                         rank = item[RANK],
                                         team = item[TEAM],
                                         year = self.year,
                                         month = self.month,
                                         day = self.day)            
            html.append(output)
        return html

    def set_day(self, year, month, day):
        '''
        当日以外の賞状を作るとき用
        年、月、日を設定
        '''
        self.year = self.get_reiwa(year, gannen = True)
        self.month = month
        self.day = day

    def get_reiwa(self, year, gannen = False):
        '''
        西暦 -> 令和　の変換
        '''
        assert year > 2018, '令和以前の日時'
        reiwa = year - 2018
        return "元" if reiwa == 1 and gannen == True else reiwa

if __name__ == '__main__':
    print("クラブ戦用賞状印刷")
