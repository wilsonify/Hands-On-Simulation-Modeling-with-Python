import numpy as np
import matplotlib.pyplot as plt

def test_smoke():
    print("fire?")

def test_bd():
    N = 1000
    n = 10
    p = 0.5
    
    P1 = np.random.binomial(n,p,N)
    
    
    plt.figure()
    plt.hist(P1, density=True, alpha=0.8, histtype='bar', color = 'green', ec='black')
    plt.show()
    
    
    