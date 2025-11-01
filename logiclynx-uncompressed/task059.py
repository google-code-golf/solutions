def p(g):
 w,r,i=[0]*9,range(11),0
 for v in sum(g,[]):w[i//44*3+i%11//4]+=v%5and(E:=v);i+=1
 return[[(5,w[i//4*3+j//4]//max(w)*E)[i%4<3>j%4]for j in r]for i in r]