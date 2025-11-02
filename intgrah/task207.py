p=lambda m:min(s:=[[m[k//8+i][k%4:][:2]for i in(0,1)]for k in b""],key=s.count)
# b"" is [4,3,24,27]
# Can't be [0,3,24,27] because null bytes not allowed