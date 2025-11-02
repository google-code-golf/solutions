p=lambda m,k=171:-k*m or p([[[v%4,v|3*(v%2>u%3),v or u&4][k>>6]for u,v in zip([4]+r,r)]for*r,in zip(*m[::-1])],k-1)
# Similar to 279
# 1. Flood fill 4s from the edges inwards, thus holes will remain 0s as they are "protected" by 1s (v or u&4)
# 2. Replace any 1 that touches a 0, or a 3, with a 3 ([v,3][v==1>u%3])
# 3. Replace all 4s with 0s (v%4)