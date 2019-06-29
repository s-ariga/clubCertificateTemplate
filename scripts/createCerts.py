#!/usr/bin/env python
# -*- coding : utf-8 -*-

import datetime
import jinja2
import pdfkit
import ParseCertificateTemplate

# テンプレート置き場
TEMPLATE_DIR = "../template/"
TEMPLATE_INDIVIDUAL = TEMPLATE_DIR + "certificate-indivi.html"
TEMPLATE_MIXTEAM = TEMPLATE_DIR + "certificate-mixteam.html"
TEMPLATE_TEAM_POSI = TEMPLATE_DIR + "certificate-tem-posi.html"
TEMPLATE_TEAM_ALL = TEMPLATE_DIR + "certificate-team-all.html"

# 成績置き場
RESULT_DIR = "../results/"
RESULT_INDIVIDUAL = RESULT_DIR + "individual.xlsx"
RESULT_MIXTEAM = RESULT_DIR + "mixteam.xlsx"
RESULT_TEAM_POSI = RESULT_DIR + "team_posi.xlsx"
RESULT_TEAM_ALL = RESULT_DIR + "team_all.xlsx"

# 出力先
OUTPUT_DIR = "../output/"
OUTPUT_TEAM_ALL = OUTPUT_DIR+"teamAll{0}.pdf"
def createCerts():
    
    
    pass

def createCertsTeamAll():

    result = pd.read_excel(RESULT_TEAM_ALL, dtype='object')
    
    html = ParseCertificateTemplate(TEMPLATE_TEAM_ALL, result)

    rank = 1
    for cert  in html.getCertificate():
        #pdfkit.from_string(cert, OUTPUT_DIR+"teamAll"+str(rank)+".pdf")
        with f in open(OUTPUT_TEAM_ALL.format(str(rank)), mode="w"):
            f.write(cert[rank])
        rank += 1
        

if __name__ == "__main__":
    createCertsTeamAll()
    
