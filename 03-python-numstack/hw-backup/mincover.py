import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxpy"], stdout=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx>=3.4"], stdout=subprocess.DEVNULL)

import networkx as nx, cvxpy, numpy as np
np.float_ = np.float64

def mincover(graph: nx.Graph)->set:
    """
    Return a minimum-cardinality vertex cover in the given graph.
    
    >>> len(mincover(nx.Graph([(1,2),(2,3)])))
    1
    >>> len(mincover(nx.Graph([(1,2),(2,3),(3,1)])))
    2
    >>> len(mincover(nx.Graph([(1,2),(2,3),(3,4),(4,1)])))
    2
    >>> len(mincover(nx.Graph([])))
    0
    """
    # Your code here
    pass


def test_mincover():
    # Your code here
    pass

if __name__ == '__main__':
    edges=eval(input())
    graph = nx.Graph(edges)
    print(len(mincover(graph)))

