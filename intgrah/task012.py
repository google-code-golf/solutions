# R=-2,-1,0,1,2
# E=enumerate
# def p(m):[exec("m[y+Y][x+X]=v*(abs(Y)==abs(X))or(Y*X==0)*r[x-1]")for y,r in E(eval(str(m)))for x,v in E(r)if m!=v>0<r[x-1]*r[x+1]for Y in R for X in R];return m
import re;p=lambda g,k=7:-k*g or p(eval(re.sub([r"0(?=(.{41})?.{37}([^0]), (.), \2.{34}\2)",r"(0)(?=(, ([^0])){3}.{32}\2)"][k//4],r"\3",str([*zip(*g[::-1])]))),k-1)
