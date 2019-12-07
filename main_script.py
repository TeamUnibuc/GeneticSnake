import torch as th
import generator
import model

M = 20000

def train(N, lr):
    fin, fout = generator.generator(M)
    model.train(fin, fout, N, lr)

fin, fout = generator.generator(1)
print("Expected", fout, ", got", float(model.frwd_pass(fin)))
