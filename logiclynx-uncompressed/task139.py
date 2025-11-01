def p(g,k=18):
 while k:a=any(g[8])*2;k-=1;R=g[k//3+1+k//9*a];R[c]=R[c:=(a,5)[k>8]+k%3]or 7
 return g