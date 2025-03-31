import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxpy"], stdout=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxopt"], stdout=subprocess.DEVNULL)

import networkx as nx, cvxpy, numpy as np, matplotlib.pyplot as plt

def mincover(graph: nx.Graph)->int:
    # Put your code here
    pass

def test_mincover():
    pass

if __name__ == '__main__':
    edges=eval(input())
    graph = nx.Graph(edges)
    print(mincover((graph))
    
