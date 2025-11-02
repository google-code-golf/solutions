import re
p=lambda g,i=7:-i*g or p(eval(re.sub(['0(?=.{22,34}1, ([2-9]), 1)','0(?=, ([2-9]))'][i>0],r'\1',str([*zip(*g[::-1])]))),i-1)