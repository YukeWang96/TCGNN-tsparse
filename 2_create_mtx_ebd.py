#!/usr/bin/env python3
import os
os.environ["PYTHONWARNINGS"] = "ignore"
import numpy as np 
from scipy import sparse, io

hidden = 16

dataset = [
        ( 'amazon0505'          , 410236  , 22),
        ( 'artist'              , 50515	  , 12),
        ( 'com-amazon'          , 548551  , 22),
        ( 'soc-BlogCatalog'	, 88784	  , 39),      
        ( 'amazon0601'  	, 403394  , 22), 
]

for data, nodes, _ in dataset:
    command = "./spmm tc-gnn/{}.mtx".format(data)
    m = sparse.csr_matrix(np.ones((nodes, hidden)))
    io.mmwrite("tc-gnn_ebd/{}.mtx".format(data), m)
    os.system(command)