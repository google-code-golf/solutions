import re
def p(a):
 s=re.sub(', ','',str(a+[*zip(*a)]));a=int(max(s,key=s.count));n={0:(0,a)}
 for t in range(10):
  if(t^a)*(o:=re.findall(f'{t}+',s)):r=len((re.findall(f'{t}{t}([^]){t}]+){t}|$',s+s[::-1]))[0]);n[len(max(o))*((r>0)+1)+r>>1]=1+r>>1,t
 return[[a*(n[s[1]][0]>s[0])or n[s[1]][1]for t in range(-max(n),max(n)+1)if(s:=sorted((abs(t),abs(o))))]for o in range(-max(n),max(n)+1)]