import io
import sys

_INPUT = """\
6
4
1161
1119
7111
1811
10
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
1111111111
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())  
for __ in range(case_no):
  N=int(input())
  A=[list(map(int,list(input()))) for _ in range(N)]
  ans=0
  d=[(i,j) for i in range(-1,2) for j in range(-1,2)]
  for i in range(N):
    for j in range(N):
      for k in range(9):
        if k==4: continue
        tmp=''
        for l in range(N):
          tmp+=str(A[(i+l*d[k][0])%N][(j+l*d[k][1])%N])
        ans=max(ans,int(tmp))
  print(ans)