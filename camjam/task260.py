# R=range(10)
# P=lambda m,k=7:-k*m or P([*zip(*[[(a:=max({*sum(m,())}-{5})if(y<1,0,0,5)==m[y][x:x+2]+m[y-1][x:x+2]else(x*y and m[y-1][x-1])|(x<9>y and m[y+1][x+1])|m[y][x])*(a!=5-9*k)for x in R]for y in R])],k-1)
# import re
# p=lambda m,k=7:-k*m or p(eval(re.sub("(?<=[^0].{34})[05]|[05](?=.{34}[^0])","k and 5",re.sub("(?<=0, 5.{28})0(?=, 0)",max({*str(m)}-{*"5[]"}),str([*zip(*m)])))),k-1)
# TODO
# from debug import *
# import re;p=lambda g,k=9:-k*g or p(eval(re.sub(*[("(?<=0, )0(?=.{28}5, 0)|0(?=.{34}[^ 05])|(?<=[^,05].{34})0",r"sum({*sum(g,g[0])}-{5})"),"50"][k<1],str([*zip(*g)]))),k-1)
# import re;p=lambda g,k=9:-k*g or p(eval(re.sub("(?<=0, )0(?=.{28}5, 0)|0(?=.{34}[^ 05])|(?<=[^,05].{34})0|5"+"5"*k,"sum({*sum(g*k,g[:0])}-{5})",str((*zip(*g),)))),k-1)
import re;p=lambda g,k=39:-k*g or p((*zip(*eval(re.sub(k%2*"(?<=0, )0(?=.{28}5, 0)|0(?=.{34}[^ 05])|"+"5"*-~k,"sum({*sum(g*k,g[:0])}-{5})",str(g)))[::-1]),),k-1)
