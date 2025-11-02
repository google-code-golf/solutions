import re
def p(e):
 e=eval(re.sub(f:=str(max(max(e))),"1",str(e)))
 for t in e*4:e=eval(re.sub(f"0(?=(.......{ {len(e)*3-2}}4)*(?<=1, 1, 4)|(.{ {len(e)*3-2}}4)*(?<=4), 1, 1|, 4[, 4]+1(?![, 4]+1)|(?<=1, 0)(, 0)*, 1, 0)","4",str([*zip(*e[::-1])])))
 return eval(re.sub("1",f,str(e)))