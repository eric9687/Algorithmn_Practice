#22866
import sys
from typing import AbstractSet

input = sys.stdin.readline

s = input().rstrip()
stack = []

l = 0
tmp = ''

for ch in s:
    # if ch == s[-1]:
    #     break

    if ch.isdigit():
        l += 1
        tmp =ch
    elif ch == '(':
        stack.append((tmp,l-1))
        l = 0
    else:
        multi, preL = stack.pop()
        l = (int(multi)*l) + preL

print(l)

# 3(2) => 222,  4(5) => 5555


# 33(562(71(9)))
# 33(562(79))
# 33(567979)
# 3567979567979567979

# stack = [(곱할 수, 더할 수)]