#!/usr/bin/env python3
"""Lint a CET-4 note for the 「两套颜色不打架」 rules (SKILL.md §二). Usage: check_prose_colors.py note.md [...]
Prose = a line that is not inside a <div> component, table, callout, heading or <details> record block.
Flags in prose: g-* role colours, kw-red / t-red used as 'wrong' colour, inline MM:SS timestamps.
"""
import re, sys
BAD = [(re.compile(r'class="g-(subj|pred|obj|adv|mod|conj|nf)"'), 'g-* 成分色出现在正文段落（只许放对照图/卡片/例句行）'),
       (re.compile(r'class="(kw-red|t-red)"'), '正文用红字（错写法请用 strike-red 或 ✗ 卡）'),
       (re.compile(r'(?<![\d.])\b\d{1,2}:\d{2}\b(?![\d.])'), '正文出现 MM:SS 时间戳（只放折叠原话/记录里）')]
def lint(path):
    n = 0; in_det = False; div = 0; fence = False
    for i, line in enumerate(open(path, encoding='utf-8', newline='').read().split('\n'), 1):
        s = line.strip()
        if s.startswith('```'): fence = not fence
        if fence: continue
        if s.startswith('<details'): in_det = True
        if in_det:
            if s.startswith('</details'): in_det = False
            continue
        opens, closes = len(re.findall(r'<div\b', s)), len(re.findall(r'</div>', s))
        was = div; div += opens - closes
        if was > 0 or opens or s.startswith(('|', '>', '#', '<table', '---', '课堂原图')) or not s: continue
        for rx, msg in BAD:
            if rx.search(s):
                print(f'{path}:{i}: {msg}\n    {s[:90]}'); n += 1
    return n
sys.exit(1 if sum(lint(p) for p in sys.argv[1:]) else 0)
