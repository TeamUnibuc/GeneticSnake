import torch as th
import torch.nn as nn

N = 100

model = nn.Sequential(
    nn.Linear(N, N),
    nn.ReLU(),
    nn.Linear(N, N),
    nn.ReLU(),
    nn.Linear(N, 1)
).cuda()

def frwd_pass(fin):
    return model(fin)

def train(fin : th.Tensor, fout : th.Tensor, epoch):
    adam = th.optim.Adam(model.parameters(), lr=1e-5)
    loss_fn = nn.L1Loss()

    for i in range(epoch):
        print("Trying epoch #", i)
        adam.zero_grad()
        loss = loss_fn(fout, model(fin))
        loss.backward()
        print("Loss: ", float(loss))
        adam.step()

