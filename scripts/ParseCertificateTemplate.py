#!/usr/bin/env python
# -*- coding : utf-8 -*-
# Seiichi Ariga <seiichi.ariga@gmail.com>

'''
クラブ戦用
賞状テンプレートを読んで、htmlとして返す
'''
import os
import jinja2
# import pandas as pd
import datetime

import Positions as posi

# 賞状の日付け
YEAR = 2024
MONTH = 11
DAY = 24

POSI = 'Position'
SCORE = 'Score'
RANK = 'Rank'
TEAM = 'Team'
NAME = 'Name'
NAME1 = 'Name1'
NAME2 = 'Name2'
NAME3 = 'Name3'

# 順位をどこまで表彰するか（最大値）
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
        print(path + " " + filename)
        assert os.path.exists(path + filename), 'テンプレートファイルが存在しない'
        self.df = data

        today = datetime.date.today()
        self.year = self._get_reiwa(today.year, gannen=True)
        self.month, self.day = today.month, today.day
        # 第35回
        self.set_day(YEAR, MONTH, DAY)

    def getCertificate(self, position='', team=False):
        '''
        テンプレートに成績を流し込み、順位順にhtmlのリストに入れて返す

        TODO: 2人以下の団体の場合、いない選手はnanという名前になる。(Jinja2を使っているため)

        parameters
        position : 種目名 デフォルト=団体
        team : 種目別団体 デフォルト=種目別個人

        returns
        html : データを流し込んだテンプレート
        '''

        assert isinstance(position, str), '種目名指定エラー'
        assert self.tmplt_file is not None, 'Class not properly initialized.'
        template = self.tmplt_env.get_template(self.tmplt_file)

        html = []
        for index, item in self.df.iterrows():
            if position in posi.POSITIONS:
                if team:
                    # 種目別団体
                    output = template.render(position=item[POSI],
                                             score=item[SCORE],
                                             rank=item[RANK],
                                             team=item[TEAM],
                                             name1=item[NAME1],
                                             name2=item[NAME2],
                                             name3=item[NAME3],
                                             year=self.year,
                                             month=self.month,
                                             day=self.day)
                else:
                    # 種目別個人
                    # チーム名と名前のフォントサイズを決める
                    print(item)
                    fontTeam = self._get_font_size(item[TEAM], default_size=45)
                    fontName = self._get_font_size(item[NAME], default_size=45)
                    if item[RANK] == 1:
                        # 秋の大会用
                        # certtype = '賞　状'
                        certtype = '第１位'
                    else:
                        certtype = '賞　状'
                    output = template.render(certtype=certtype,
                                             position=item[POSI],
                                             score=item[SCORE],
                                             rank=item[RANK],
                                             team=item[TEAM],
                                             name=item[NAME],
                                             fontTeam=self._font_size(
                                                 fontTeam),
                                             fontName=self._font_size(
                                                 fontName),
                                             year=self.year,
                                             month=self.month,
                                             day=self.day)
            elif position in posi.ARMIX:
                # ミックスチーム
                output = template.render(score=item[SCORE],
                                         rank=item[RANK],
                                         team=item[TEAM],
                                         name1=item[NAME1],
                                         name2=item[NAME2],
                                         year=self.year,
                                         month=self.month,
                                         day=self.day)
            else:
                # 総合団体
                fs = self._get_font_size(item[TEAM], default_size=60)
                output = template.render(score=item[SCORE],
                                         rank=item[RANK],
                                         team=item[TEAM],
                                         year=self.year,
                                         month=self.month,
                                         day=self.day,
                                         fontSize=self._font_size(fs))
            html.append(output)
        return html

    def set_day(self, year, month, day):
        '''
        当日以外の賞状を作るとき用
        年、月、日を設定
        '''
        self.year = 6 # self._get_reiwa(year, gannen=True)
        self.month = 11 # month
        self.day = 24 # day

    def _get_reiwa(self, year, gannen=False):
        '''
        西暦 -> 令和　の変換
        '''
        assert year > 2018, '令和以前の日時'
        reiwa = year - 2018
        return "元" if reiwa == 1 and gannen else reiwa

    def _get_font_size(self, string, default_size=50):
        '''
        1行に収まるフォントサイズを計算する(だいたい１１文字)
        '''
        WIDTH = 600
        print("font size: "+str(string))
        font_size = int(WIDTH / len(string))
        print('Team Name: {0} len: {1} font-size: {2}'.format(string,
                                                              len(string),
                                                              font_size))
        return font_size if font_size < default_size else default_size

    def _font_size(self, fs):
        return 'font-size:{0}px;'.format(fs)


if __name__ == '__main__': # これはライブラリ
    print("クラブ戦用賞状印刷用ライブラリ")
