_accepted = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901'";:<>1?() \n'''

def GenerateGext():
    fin = open("shakespeare.txt", "r")
    fout = open("text.txt", "w")

    last = ''
    for c in fin.read():
        if c in _accepted and not(last in " \n" and last == c):
            fout.write(c)
        last = c
    fout.flush()


if __name__ == '__main__':
    GenerateGext()