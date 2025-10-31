import re
p=lambda g,d="0, "*9:eval(d.join(re.sub('(?<=4.{34})4(?=.{34}4)','12'[w.count("4")*2>str(g).count("4")],w)for w in str(g).split(d)))