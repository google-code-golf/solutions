import re
def p(s):
 for t in range(31,24,-1):
  for n in range(31,3,-1):
   for r in range(31-n):
    for f in range(31-t):
     for n in range(n-n*any(any(r[f and f-1:f+t+1])for r in s[r and r-1:r+n+1])):s[r+n][f:f+t]=[3]*t
 for n in range(31,24,-1):
  for t in range(31,3,-1):
   for r in range(31-n):
    for f in range(31-t):
     for n in range(n-n*any(any(r[f and f-1:f+t+1])for r in s[r and r-1:r+n+1])):s[r+n][f:f+t]=[3]*t
 for t in range(312):s=eval(re.sub("(?<=(3, ){4})0(?=(, (?<![^0].{91})0(?!.{91}[^0]))*\))","3",str([*zip(*s[::-1])])))
 return s