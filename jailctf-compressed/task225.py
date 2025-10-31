import re
p=lambda g:eval(re.sub(r'0(?=(.{19}0)?(, 0)?.{22}([^0]).{22}(?!\3|0)(\d))',r'\4',f'{*zip(*g[42:]or p(g*2)),}'))[::-1]