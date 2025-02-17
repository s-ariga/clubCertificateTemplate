# Seiichi Ariga <seiichi.ariga@gmail.com>

# 賞状の印刷
# AR60PRは、秋はやらない
# FR3x20, R3x20への対応 : 2022/07

# *総合団体* は最終日に印刷、閉会式で配る
# python .\createCerts.py -c
# 種目別は郵送
python .\createCerts.py -t -p ARM
python .\createCerts.py -t -p ARW
python .\createCerts.py -t -p R3PM
python .\createCerts.py -t -p R3PW
python .\createCerts.py -t -p RPRM
python .\createCerts.py -t -p RPRW
# 大口径の大会用 2023/10/14
# python .\createCerts.py -t -p FR3X20
# python .\createCerts.py -t -p FR60PR
# python .\createCerts.py -p FR40PR
# python .\createCerts.py -p FR20PR
# 秋はやらないので、コメントアウト1
# python .\createCerts.py -t -p ARPR
# python .\createCerts.py -t -p ARMIX
# python createCerts.py -p R1
# python createCerts.py -p R4
# python createCerts.py -p R6
