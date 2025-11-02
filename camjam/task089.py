def p(i):
    z=[[*d]for d in i]
    for b in range(11):
        for w in range(11):
            for n in range(11):
                for d in range(11):
                    r=[i[b+f//3][n+f%3]for f in range(9)]
                    e=[z[w+f//3][d+[2-f%3,f%3][3in r]]for f in range(9)]
                    if any({*e}&{*r}&{2,3})*all(f in[e,0]for e,f in zip(e,r))*any(e[1::3])*any(e[3:6])*(2<abs(d-n)or w!=b):
                        for f in range(9):i[b+f//3][n+f%3]=e[f]
    return i