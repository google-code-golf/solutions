p=lambda m:[m:=[*zip(*[*m[:(y:=str(m).index('2')//14)],*filter(any,m[y:]),[8*('3'in str(m[y:]))]*5,*[[0]*5]*12][len(m)-1::-1])]for _ in m][3]
# TODO: better way to do this