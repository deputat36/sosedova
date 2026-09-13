#!/usr/bin/env python3
"""Read-only live deployment check; never submits a customer enquiry."""
from urllib.request import urlopen
from pathlib import Path
import sys
base='https://'+Path('CNAME').read_text().strip()
try:
 for path,needle in [('/', 'Соседова'),('/robots.txt',base+'/sitemap.xml'),('/sitemap.xml',base+'/'),('/online-zayavka/','data-online-application'),('/kalkulyator-ipoteki/','data-mortgage-calc')]:
  with urlopen(base+path,timeout=20) as response:
   html=response.read().decode();assert response.status==200 and needle in html,(path,'unexpected deployment')
   assert 'sterlikova' not in html and 'Татьяна' not in html,(path,'wrong identity')
  print('OK',base+path)
except Exception as e:print('Live domain not verified:',e);sys.exit(1)
