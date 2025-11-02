R=range(11)
p=lambda m:next(a for k in R if str(a:=[[[m[k//3*4+i//4][k%3*4+j//4],5][m[i][j]==5]for j in R]for i in R]).count('0')>44)
# We use next instead of [0], because "for k in R" is 11 iterations, but k is really supposed to run for 9 iterations.