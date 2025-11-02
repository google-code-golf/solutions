p=lambda m,k=19:-k*eval(str(m).replace(*"10"))or p([*zip(*m[:8-8*max(m[0]):-1])],k-1)
# Alternatives
# p=lambda m,k=23:-k*m or p([*zip(*eval(str(m).replace(*"10"))[:-7*max(m[0]):-1])],k-1)
# p=lambda m,k=23:-k*m or p([*zip(*eval(str(m).replace(*"10"))[any(m[-1])-2::-1])],k-1)