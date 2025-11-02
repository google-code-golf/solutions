p=lambda m:max([(-(f:=sum(c:=[r[k%10:k//10%10+1]for r in m[k//100%10:k//1000+1]],m).count)(0),f(2),f(1)+f(8),c)for k in range(10000)])[3]
# Similar to 216
# Check every submatrix
# Ensure it has no 0s
# Maximise number of 2s first, and break ties by number of 1s and 8s