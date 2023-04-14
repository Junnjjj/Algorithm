# import sys
# input = sys.stdin.readline

# def GCD(x,y):
#     if y == 0:
#         return x
#     else:
#         return GCD(y, x%y)

# s = input().rstrip()
# t = input().rstrip()
# gcd = GCD(len(s),len(t))
# lcm = len(s) * len(t) // gcd

# print(gcd, lcm)

# s = s * (lcm // len(s))
# t = t * (lcm // len(t))
# if s == t:
#     print(1)
# else:
#     print(0)
