def p(s):
 for e,n in sorted([[-i.count(2),i]for l in range(len(s)-2)for r in range(len(s[0])-2)if all(i:=[s[l+e][r+f]for e in range(3)for f in range(3)])and{*i}!={2}!=[2for e in range(3)for f in range(3)for s[l+e][r+f]in[0]]]):
  for e in range(4):[[2for e in range(3)for f in range(3)for s[l+e][r+f]in[n[e*3+f]]]for l in range(len(s)-2)for r in range(len(s[0])-2)if all(s[l+e][r+f]==2!=n[e*3+f]or n[e*3+f]-s[l+e][r+f]==2in s[l+e]for e in range(3)for f in range(3))];s=[s[::-1]for*s,in zip(*s)if 2in s]
 return s
# ----------------------------------------------------------------
# compression: auto
# jailctf
