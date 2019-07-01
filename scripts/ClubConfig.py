# -*- coding : utf-8 -*-

'''
ファイル関係の設定
'''

'''
テンプレート変数
{{ Position }} : 種目名 (Positions.py参照)
{{ Score }} : 点数
{{ Rank }} : 順位
{{ Team }} : チーム名
{{ Name }} : 個人氏名
{{ Name1 }} : 種目別団体氏名 MixTeam氏名
{{ Name2 }} : 種目別団体氏名 MixTeam氏名
{{ Name3 }} : 種目別団体氏名
'''

# テンプレート置き場ディレクトリ
TEMPLATE_DIR = "../template/"
# テンプレートファイル名
TEMPLATE_INDIVIDUAL = "certificate-indivi.html"
TEMPLATE_MIXTEAM = "certificate-mixteam.html"
TEMPLATE_TEAM_POSI = "certificate-team-posi.html"
TEMPLATE_TEAM_COMBI = "certificate-team-combi.html"

# 成績置き場ディレクトリ
RESULT_DIR = "../results/"
# 成績ファイル名
RESULT_INDIVIDUAL = RESULT_DIR + "individual.xlsx"
RESULT_MIXTEAM = RESULT_DIR + "mixteam.xlsx"
RESULT_TEAM_POSI = RESULT_DIR + "team-position.xlsx"
RESULT_TEAM_COMBI = RESULT_DIR + "team_combi.xlsx"

# 出力先ディレクトリ
OUTPUT_DIR = "../output/"
# 出力ファイル名
OUTPUT_INDIVIDUAL = OUTPUT_DIR+"Individual{0}-{1}.html"
OUTPUT_MIXTEAM = OUTPUT_DIR+"MixTeam{0}-{1}.html"
OUTPUT_TEAM_POSITION = OUTPUT_DIR+"Team{0}-{1}.html"
OUTPUT_TEAM_COMBI = OUTPUT_DIR+"TeamCombined{0}-{1}.html"
