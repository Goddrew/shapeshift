import numpy as np 

def neighbors(): 
    """Obtain current state space neighbors
    """
    pass 

def cost(yhat, y): 
    """Return the scalar cost between prediction (yhat) and true image (y)
    """
    yhat = yhat.flatten() 
    y = y.flatten() 
    m = len(yhat)
    cost = np.sum(np.square(y - yhat), keepdims=False) 
    cost = 1/m * cost 
    return cost # 

