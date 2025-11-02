p=lambda m:[(s:=1)*[(s:=(1^-s^v)%3)*~v%5%4for v in r]for r in m]
# p=lambda m:[(s:=1)*[3*((s:=9&6-s%5<<v)==v)for v in r]for r in m]

# Mealy machine
# A = 1, B = 2, C = 0
#        --------- 0/0 ---------
#      /                        \
#     v                          \
# --> A --- 2/0 --> B --- 2/0 --> C
#    ^ |           ^ |           ^ |
#    | |           | |           | |
#    0/0           0/3           2/0

# const A: Num = 1;
# const B: Num = 2;
# const C: Num = 0;
# 
# // Next state (S = old state, V = value)
# pub const S: &[Num] = &[A, A, B, B, C, C];
# pub const V: &[Num] = &[0, 2, 0, 2, 0, 2];
# pub const G: &[Num] = &[A, B, B, C, A, C];
# 
# // Output (S = new state, V = value)
# pub const S: &[Num] = &[A, B, B, C];
# pub const V: &[Num] = &[0, 2, 0, 2];
# pub const G: &[Num] = &[0, 0, 3, 0];
#
# Tried:
# A = 0, B = 1, C = 2
# A = 1, B in range(-2, 10), C in range(-2, 10)