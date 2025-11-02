import re
p=lambda g:[g:=eval(re.sub('[02], [02](.{52})%s, 0'%c,r'2,2\1 2,2',str(g),2))for c in'020000'][5]