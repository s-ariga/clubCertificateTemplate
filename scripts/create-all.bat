@echo off
rem 全部の賞状を作成する
rem 秋はAR60PR, AR40PRはやらない
python createCerts.py -m
python createCerts.py -c
python createCerts.py -t -p AR60
python createCerts.py -t -p AR60W
python createCerts.py -t -p FR3X40
python createCerts.py -t -p R3X40
python createCerts.py -t -p FR60PR
python createCerts.py -t -p R60PR
python createCerts.py -t -p AR60PR
python createCerts.py -p AR40PR
python createCerts.py -p R1
python createCerts.py -p R4
python createCerts.py -p R6
