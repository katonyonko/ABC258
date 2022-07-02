import io
import sys

_INPUT = """\
6
4
0011
0011
1101
1110
10
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
0000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def Popcount(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c
  N=int(input())
  A=[input() for _ in range(N)]
  A=[sum([1<<j for j in range(N) if A[i][j]=='1']) for i in range(N)]
  ans=0
  for i in range(N):
    for j in range(i+1,N):
      if (A[i]>>j)&1==0: continue
      ans+=Popcount(A[i]&A[j])
  print(ans//3)