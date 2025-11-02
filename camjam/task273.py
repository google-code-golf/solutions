import re;p=lambda g,k=15:-k*g or p(eval(re.sub(*["30",(f"(?<=[{k%2*2+2}3], )0(?=[^)]*[34])","23"[k%2])][k>0],str([*zip(*g)]))),k-1)
