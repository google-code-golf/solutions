p=lambda m:[*zip(*(a:=[*zip(*m)]+m[::-1]))]+[*zip(*a[::-1])][::-1]
# p=lambda m:[*zip(*(a:=m+[*zip(*m)][::-1])[::-1])]+[*zip(*a)][::-1]
# Same as 106