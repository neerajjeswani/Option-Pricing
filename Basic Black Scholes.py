def call(s,k,r,v,t):
    
    import numpy as np
    from scipy.stats import norm
    
    t = t/253
    
    d1 = (np.log(s/k) + (r + (v**2)/2)*t) / (np.sqrt(t)*v)
    d2 = d1 - np.sqrt(t)*v
    
    c = s*norm.cdf(d1) - k*np.exp(-r*t)*norm.cdf(d2)
    
    return c



def put(s,k,r,v,t):
    
    import numpy as np
    from scipy.stats import norm
    
    t = t/253
    
    d1 = (np.log(s/k) + (r + (v**2)/2)*t) / (np.sqrt(t)*v)
    d2 = d1 - np.sqrt(t)*v
    
    p = k*np.exp(-r*t)*norm.cdf(-d2) - s*norm.cdf(-d1)
    
    return p