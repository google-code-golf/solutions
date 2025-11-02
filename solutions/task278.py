p=lambda m,k=11:-k*m or p([[[v%9,v|3%-~u,v<<u][k>>2]for u,v in zip([0]+r,r)]for*r,in zip(*m[::-1])],k-1)
# ----------------------------------------------------------------
# camjam

# Bump up adjacent 2s (2<<2==8, 2<<8==512)
# Set 0s adjacent to 8 or 512 to 3 ()
# Convert 8s and 512s back to 2s
