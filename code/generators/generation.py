import pandas as pd
import numpy as np

    ## Model code
    # def gen1():
    #     with open('hugedata.txt') as f:
    #         for line in f:
    #             yield line

    # g = gen1()
    # g2 = (process(x) for x in g)
    # for x in g2:
    #     print x

catiline = 'catiline.txt'

def view(path):
    with open(path, encoding='UTF-8', newline='\r\n') as f:
        for L in f:
            yield L

t = view(catiline)

next(t)
