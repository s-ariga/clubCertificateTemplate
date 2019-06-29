#!/usr/bin/env python
# -*- coding : utf-8 -*-

'''
クラブ戦用
賞状テンプレートを読んで、htmlとして返す
'''

import jinja2
import pandas as pd

class ParseCertificateTemplate():
    def __init__(self, path, data):
        self.tmplt_loader = jinja2.FileSystemLoader(searchpath="./")
        self.tmplt_env = jinja2.Environment(loader=self.tmplt_loader)

        self.tmplt_file =  path
        self.df = data
      
    def getCertificate(self):
        '''
        テンプレートに成績を流し込み、順位順にhtmlのリストに入れて返す
        '''
        assert self.tmplt_file is not None, 'Class not properly initialized.'
        html = []

        return html
