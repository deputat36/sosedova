#!/usr/bin/env python3
"""Acceptance of actual Jekyll output: identity, SEO, URLs, privacy and service coverage."""
import json,re,sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote,urljoin
from xml.etree import ElementTree as ET
ROOT=Path(sys.argv[1] if len(sys.argv)>1 else '_site')
DOMAIN='https://'+(ROOT/'CNAME').read_text().strip()
errors=[]
def check(ok,message):
 if not ok:errors.append(message)
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__(convert_charrefs=True);self.tags=[];self.json=[];self.active=False;self.block='';self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags.append((tag,a))
  if tag=='script' and a.get('type')=='application/ld+json':self.active=True;self.block=''
 def handle_data(self,data):
  if self.active:self.block+=data
 def handle_endtag(self,tag):
  if tag=='script' and self.active:self.json.append(self.block);self.active=False
 def find(self,tag,**attrs):return [a for t,a in self.tags if t==tag and all(a.get(k)==v for k,v in attrs.items())]
urls={};titles={};descriptions={};total=0
for path in ROOT.rglob('*.html'):
 text=path.read_text();p=Page(text);rel='/'+path.relative_to(ROOT).as_posix();url=rel.removesuffix('index.html') if rel.endswith('/index.html') else rel
 urls[url]=p;total+=1
 check(not re.search(r'Татьян|Стерлик|sterlik|tatyan|9030250807|c6b147c0|__BROKER_|__SITE_URL__|\{\{|\{%|Liquid Exception',text,re.I),f'{url}: inherited identity or unrendered template')
 canon=p.find('link',rel='canonical');check(len(canon)==1 and canon[0].get('href','').startswith(DOMAIN+'/'),f'{url}: canonical')
 robots=p.find('meta',name='robots');noindex=any('noindex' in a.get('content','') for a in robots)
 if not noindex:
  check(len(p.find('h1'))==1,f'{url}: exactly one H1 required')
  title=re.search(r'<title>(.*?)</title>',text,re.S);title=title[1].strip() if title else ''
  check(bool(title),f'{url}: missing title');check(title not in titles,f'{url}: duplicate title with {titles.get(title)}');titles[title]=url
  desc=p.find('meta',name='description');check(bool(desc and desc[0].get('content')),f'{url}: description')
  if desc:
   value=desc[0]['content'];check(value not in descriptions,f'{url}: duplicate description with {descriptions.get(value)}');descriptions[value]=url
  check(bool(p.find('meta',property='og:image')),f'{url}: missing OpenGraph')
  check(canon and canon[0].get('href')==DOMAIN+url,f'{url}: self canonical')
  check(not re.search(r'Борисоглеб|Грибанов|Поворино|ЭТАЖИ',text),f'{url}: obsolete regional/employer claim')
 for block in p.json:
  try:
   parsed=json.loads(block);check(isinstance(parsed,dict),f'{url}: JSON-LD object expected')
  except ValueError as e:errors.append(f'{url}: JSON-LD {e}')
 for tag,a in p.tags:
  if tag=='img':check('alt' in a and 'width' in a and 'height' in a,f'{url}: image accessibility/layout dimensions')
  references=[]
  if tag=='a':references.append(a.get('href',''))
  if tag in ('script','img'):references.append(a.get('src',''))
  if tag=='link':references.append(a.get('href',''))
  if tag=='meta' and a.get('property')=='og:image':references.append(a.get('content',''))
  for href in references:
   if not href:continue
   parsed=urlparse(urljoin(DOMAIN+url,href))
   if parsed.scheme not in ('http','https') or parsed.netloc!=urlparse(DOMAIN).netloc:continue
   file=ROOT/unquote(parsed.path).lstrip('/')
   if parsed.path.endswith('/'):file=file/'index.html'
   check(file.is_file(),f'{url}: broken internal reference {href}')
# All declared services are reachable and contain a conversion route and FAQ.
for url,p in urls.items():
 if url.startswith('/uslugi/') and url!='/uslugi/' and not p.find('meta',**{'http-equiv':'refresh'}):
  check(any('/online-zayavka/' in a.get('href','') for a in p.find('a')),f'{url}: missing lead route')
  check(bool(p.find('details')),f'{url}: missing visible FAQ')
# No public source/backend leakage; static data stays private until explicitly sent.
for name in ('supabase','scripts','docs','_data'):
 check(not (ROOT/name).exists(),f'Published internal directory: {name}')
form=(ROOT/'online-zayavka/index.html').read_text();f=Page(form)
for name in ('client_name','phone','consent'):
 check(any('required' in a for a in f.find('input',name=name)),f'form: {name} must be required')
check(any('required' in a for a in f.find('select',name='scenario')),'form: required goal')
check('c6b147c0' not in form,'old recipient still configured')
check('application-runtime-fallback' in form,'form: no progressive fallback')
for a in f.find('form'):
 if 'data-online-application' in a and a.get('data-lead-mode')=='disabled':
  check(not a.get('data-web3forms-access-key') and not a.get('data-lead-endpoint'),'disabled form leaks old delivery config')
try:
 tree=ET.parse(ROOT/'sitemap.xml');locs=[e.text for e in tree.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
 check(len(locs)>=65,'sitemap unexpectedly lost content');check(len(locs)==len(set(locs)),'duplicate sitemap URLs')
 for loc in locs:
  url=urlparse(loc).path;check(loc.startswith(DOMAIN+'/') and url in urls,f'sitemap invalid URL: {loc}')
  if url in urls:check(not any('noindex' in a.get('content','') for a in urls[url].find('meta',name='robots')),f'sitemap includes noindex: {url}')
except Exception as e:errors.append(f'sitemap: {e}')
check(DOMAIN+'/sitemap.xml' in (ROOT/'robots.txt').read_text(),'robots sitemap host')
for p in ROOT.glob('assets/css/*.css'):
 for asset in re.findall(r'url\([\'"]?(/[^)\'" ]+)',p.read_text()):check((ROOT/asset.lstrip('/')).is_file(),f'{p.name}: missing CSS asset {asset}')
for e in errors:print('FAIL:',e)
print(f'Broker acceptance: {total} HTML pages, {len(errors)} errors')
sys.exit(bool(errors))
