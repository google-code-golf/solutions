# R=range(2,12);p=lambda g:[[[0,2,c:=min(f:=sum(g,[]),key=f.count)][(0<i-(k:=f.index(c))//10<4>j-k%10>0)+(k+22==i*10+j)]for j in R]for i in R]
p=lambda g:[*zip(*[([0,2,c:=min(f:=sum(g,[]),key=f.count)][(abs(i-(k:=f.index(c)))//9<2>abs(i%10-k%10))+(k==i)]for i in range(100))]*10)]
# def p(m):
# 	c=min(f:=sum(m,[]),key=f.count);k=f.index(c);a=100*[0]
# 	for i in range(9):a[k-11+i//3*10+i%3]=2
# 	a[k]=c;return[*zip(*[iter(a)]*10)]
