import re
p=lambda g:[p,eval][''in g](re.sub('0(?=(.{76})*(.{40}|(...){25,27})8)','5',str(g)[::-1]))