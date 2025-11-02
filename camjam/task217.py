p=lambda m,k=1:[[a&b for a in r for b in s]for r in-k*m for s in m]or p([*zip(*filter(any,m))],k-1)
# A mashup of tasks 1 and 31