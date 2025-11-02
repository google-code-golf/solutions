import re
def p(i):
	a={0:(0,i:=int(max(r:=re.sub(', ','',str(i+[*zip(*i)])),key=r.count)))}
	for m in range(10):
		if(m!=i)*(e:=re.findall(f'{m}+',r+r[::-1])):n=len(max(re.findall(f'{m}{m}([^]){m}]+){m}|$',r+r[::-1])));a[len(max(e))*(1+(n>0))+n>>1]=1+n>>1,m
	return[[i*(a[max(abs(m),abs(e))][0]>min(abs(m),abs(e)))or a[max(abs(m),abs(e))][1]for m in range(-max(a),max(a)+1)]for e in range(-max(a),max(a)+1)]