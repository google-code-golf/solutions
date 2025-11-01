def p(o,e=enumerate):
 (i,z),(f,u)=[(i,z)for i,r in e(o)for z,n in e(r)if n];q=u-z>>1
 if i-f:
  return[[*r]for r in zip(*p([[*r]for r in zip(*o)]))]
 n,e=u,-1
 for r in o[i-2:i+3]:o[i-2][f:=n+e*q]=o[i+2][f]=r[f-e]=o[i][n];o[i][n:f:e]=[o[i][n]]*q
 n,e=z,1
 for r in o[i-2:i+3]:o[i-2][f:=n+e*q]=o[i+2][f]=r[f-e]=o[i][n];o[i][n:f:e]=[o[i][n]]*q
 return o