import io
import sys

_INPUT = """\
6
3 3
abc
2 2
1 1
2 2
10 8
dsuccxulnl
2 4
2 7
1 2
2 7
1 1
1 2
1 3
2 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,Q=map(int,input().split())
  S=input()
  m=0
  for _ in range(Q):
    d,x=map(int,input().split())
    if d==1: m+=x
    else: print(S[(x-m-1)%len(S)])