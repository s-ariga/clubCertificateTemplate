#!/usr/bin/env python
# -*- coding : utf-8 -*-
# Seiichi Ariga <seiichi.ariga@gmail.com>

import pdfkit
import sys
import os

html = sys.argv[1]

html_base = os.path.splitext(html)[0]

pdf_out = html_base + '.pdf'

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

pdfkit.from_file(html, pdf_out, configuration=config)
