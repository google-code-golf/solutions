f=filter
p=lambda g:[*f(any,zip(*f(any,zip(*[[x&y for x in a for y in b]for a in g for b in g]))))]