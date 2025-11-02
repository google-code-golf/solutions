p=lambda m:[[i&-v//i for i,v in zip([-1,4]*9,r)]for r in m]
# Alternative
# p=lambda m:[(i:=4)and[(i:=3-i)&-v//i for v in r]for r in m]