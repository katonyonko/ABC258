import io
import sys

_INPUT = """\
6
3 4
3 4
2 3
4 2
10 1000000000
3 3
1 6
4 7
1 8
5 7
9 9
2 4
6 4
5 1
3 1
1 100
1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  stage=[list(map(int,input().split())) for _ in range(N)]
  ans=10**100
  tmp=0
  for i in range(N):
    if i>=X: break
    tmp+=sum(stage[i])
    ans=min(ans,tmp+(X-i-1)*stage[i][1])
  print(ans)