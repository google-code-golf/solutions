f=enumerate
def p(s):
	t,e=divmod(sum(s,[]).index(max({*(o:=sum([i[5:-5]for i in s[6:9]],[]))}-{0},key=o.count)),len(s))
	for i,o in f(s):
		for n,o in f(o):
			if o:s[o:=2*t+2-i][u:=2*e+2-n]=s[i][u]=s[o][n]=o
	return s
