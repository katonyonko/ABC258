import io
import sys

_INPUT = """\
6
3 2 5
3 4 1
1
2
10 5 20
5 8 5 9 8 7 4 4 8 2
1
1000
1000000
1000000000
1000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import accumulate
  from bisect import bisect_left
  N,Q,X=map(int,input().split())
  W=list(map(int,input().split()))
  s=sum(W)
  n=X//s
  r=X-n*s
  tmp=[0]+list(accumulate(W+W))
  idx=[bisect_left(tmp,tmp[i]+r)-i+n*N for i in range(N)]
  tmp=[]
  used=set()
  now=0
  while now not in used:
    tmp.append(idx[now])
    used.add(now)
    now=(now+idx[now])%N
  tail=[]
  now2=0
  while now2!=now:
    tail.append(now2)
    now2=(now2+idx[now2])%N
  loop=[now]
  now2=(now+idx[now])%N
  while now2!=now:
    loop.append(now2)
    now2=(now2+idx[now2])%N
  for _ in range(Q):
    K=int(input())
    if K<=len(tail): print(idx[tail[K-1]])
    else: print(idx[loop[(K-1-len(tail))%len(loop)]])