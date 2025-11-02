p=lambda m,*k:[[max(r[x%10::10])for x in range(len(r))]for r in zip(*k or p(m,*m))]
