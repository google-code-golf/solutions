import re
p=lambda g,i=79:-i*g or p(eval(re.sub("0(?=.{40}[38].{40}[238])","3",str([*zip(*g[::-1])]))),i-1)