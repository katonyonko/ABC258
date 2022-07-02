import io
import sys

_INPUT = """\
6
63
45
100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  K=int(input())
  h=21+K//60
  m=0+K%60
  print(h,':',str(m).zfill(2),sep='')