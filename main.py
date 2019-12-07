import torch as th
import generator
import model
import subscripts.main_script

subscripts.main_script.main_script()


M = 20000

def train(N, lr):
    fin, fout = generator.generator(M)
    model.train(fin, fout, N, lr)

