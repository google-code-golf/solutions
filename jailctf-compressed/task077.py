import re
p=lambda g,i=23:g*-i or p(eval(re.sub('(?<=[24], )[^2](?=, 2|.%s.[24])'%{len(g)*3},'4',f"{*zip(*g[::-1]),}")),i-1)