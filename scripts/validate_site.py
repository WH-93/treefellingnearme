#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = []
        self.h1 = []
        self.desc = []
        self.links = []
        self.scripts = []
        self._capture = None
        self._script_type = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title': self._capture = 'title'
        elif tag == 'h1': self._capture = 'h1'; self.h1.append('')
        elif tag == 'meta' and attrs.get('name') == 'description': self.desc.append(attrs.get('content',''))
        elif tag == 'a' and attrs.get('href'): self.links.append(attrs['href'])
        elif tag == 'script': self._script_type = attrs.get('type'); self._capture = 'script' if self._script_type == 'application/ld+json' else None
    def handle_endtag(self, tag):
        if tag in ('title','h1','script'): self._capture = None
    def handle_data(self, data):
        if self._capture == 'title': self.title.append(data)
        elif self._capture == 'h1' and self.h1: self.h1[-1] += data
        elif self._capture == 'script':
            if not self.scripts: self.scripts.append('')
            self.scripts[-1] += data


def local_target(href):
    if href.startswith(('#','tel:','mailto:','javascript:')): return None
    p = urlparse(href)
    if p.netloc and p.netloc != 'treefellingnearme.co.uk': return None
    path = p.path
    if path in ('','/'): return ROOT / 'index.html'
    candidate = ROOT / path.lstrip('/')
    if path.endswith('/'): candidate = candidate / 'index.html'
    return candidate

errors=[]; rows=[]; seen_titles={}; seen_h1={}
files=sorted(ROOT.glob('*/index.html')) + [ROOT/'index.html']
for f in files:
    text=f.read_text(encoding='utf-8')
    p=PageParser(); p.feed(text)
    title=''.join(p.title).strip(); h1=' '.join(x.strip() for x in p.h1).strip(); desc=(p.desc or [''])[0]
    words=len(re.findall(r"\b[\w’'-]+\b", re.sub(r'<[^>]+>',' ',text)))
    rel=str(f.relative_to(ROOT))
    if len(p.h1)!=1: errors.append(f'{rel}: expected 1 H1, got {len(p.h1)}')
    if len(p.desc)!=1: errors.append(f'{rel}: expected 1 description, got {len(p.desc)}')
    if not title: errors.append(f'{rel}: missing title')
    if not (35 <= len(title) <= 65): errors.append(f'{rel}: title length {len(title)}')
    if not (110 <= len(desc) <= 165): errors.append(f'{rel}: description length {len(desc)}')
    if title in seen_titles: errors.append(f'{rel}: duplicate title with {seen_titles[title]}')
    if h1 in seen_h1: errors.append(f'{rel}: duplicate H1 with {seen_h1[h1]}')
    seen_titles[title]=rel; seen_h1[h1]=rel
    if f != ROOT/'index.html' and words < 700: errors.append(f'{rel}: only {words} words')
    for script in p.scripts:
        try: json.loads(script)
        except Exception as e: errors.append(f'{rel}: invalid JSON-LD: {e}')
    for href in p.links:
        target=local_target(href)
        if target and not target.exists(): errors.append(f'{rel}: broken link {href} -> {target.relative_to(ROOT)}')
    rows.append((rel, len(title), len(desc), words, h1))

sitemap=(ROOT/'sitemap.xml').read_text(encoding='utf-8')
for f in files:
    if f == ROOT/'index.html': url='https://treefellingnearme.co.uk/'
    else: url='https://treefellingnearme.co.uk/'+f.parent.name+'/'
    if url not in sitemap: errors.append(f'sitemap missing {url}')

print(f'Validated {len(files)} pages')
for rel,tl,dl,w,h in rows: print(f'{rel:24} title={tl:2} desc={dl:3} words={w:4} H1={h}')
if errors:
    print('\nFAIL')
    for e in errors: print('- '+e)
    sys.exit(1)
print('\nPASS: titles, descriptions, H1s, JSON-LD, internal links and sitemap')
