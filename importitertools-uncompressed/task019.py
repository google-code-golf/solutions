import re
p=lambda g,i=7:-i*g or p([*zip(*eval(re.sub(f"0(?=.{ {len(g[0])*3+4}}[1-79])","8",str(g*-~(i>5)))))][::-1],i-1)