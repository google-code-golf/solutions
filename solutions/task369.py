p=lambda g,n=7:g*-n or[*map(lambda*r,b=5:[b:=a*(a>4)or[a+b//4-.25,min(a,b)][n>3]for a in r],*p(g,n-1)[::-1])]
# ----------------------------------------------------------------
# many

# cgi
p=lambda g,n=7:g*-n or[*map(lambda*r,b=5:[b:=a*(a>4)or[a+b//4-.25,min(a,b)][n>3]for a in r],*p(g,n-1)[::-1])]
# jailctf
import re;p=lambda g:exec(r"g[::-1]=zip(*eval(re.sub('(2|3), [31]|0',r'*7%3\1%5*[3\1%31]',str(g))));"*12)or g
# oxjam
p=lambda g,k=-11,z=1:k*g or[[P:=v&7or[z:=z*8,4-v%7,P&~5|v][k>>3]for v in[5]+r][:0:-1]for*r,in zip(*p(g,k+1))]
