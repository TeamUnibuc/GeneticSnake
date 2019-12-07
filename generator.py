import torch as th

N = 100
val = th.randn(1, N)

def generator(M):
    v = th.randn(M, N)
    ans = (val * v).sum(dim=[1])
    return (v, ans)