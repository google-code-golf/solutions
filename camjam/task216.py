p=lambda m:max([(-(f:=sum(c:=[r[k%20:k//20%20+1]for r in m[k//400%20:k//8000+1]],m).count)(0),f(2),f(1),c)for k in range(160000)])[3]
# Check every submatrix
# Ensure it has no 0s
# Maximise number of 2s first, and break ties by number of 1s