def call(s,k,r,v,t,d):
    
    import numpy as np
    from scipy.stats import norm
    
    t = t/253
    
    q = np.log(1+d/s)
    
    d1 = (np.log(s/k) + (r - q + (v**2)/2)*t) / (np.sqrt(t)*v)
    d2 = d1 - np.sqrt(t)*v
    
    c = s*np.exp(-q*t)*norm.cdf(d1) - k*np.exp(-r*t)*norm.cdf(d2)
    
    return c



def put(s,k,r,v,t,d):
    
    import numpy as np
    from scipy.stats import norm
    
    t = t/253
    
    q = np.log(1+d/s)
    
    d1 = (np.log(s/k) + (r - q + (v**2)/2)*t) / (np.sqrt(t)*v)
    d2 = d1 - np.sqrt(t)*v
    
    p = k*np.exp(-r*t)*norm.cdf(-d2) - s*np.exp(-q*t)*norm.cdf(-d1)
    
    return p




def call(s,k,r,v,t,d1,d2,d3,d4):
    
    import numpy as np
    from scipy.stats import norm
    
    t = t/253
    
    q = np.log(1+(d1+d2+d3+d4)/s)
    
    d1 = (np.log(s/k) + (r - q + (v**2)/2)*t) / (np.sqrt(t)*v)
    d2 = d1 - np.sqrt(t)*v
    
    c = s*np.exp(-q*t)*norm.cdf(d1) - k*np.exp(-r*t)*norm.cdf(d2)
    
    return c



def put(s,k,r,v,t,d1,d2,d3,d4):
    
    import numpy as np
    from scipy.stats import norm
    
    t = t/253
    
    q = np.log(1+(d1+d2+d3+d4)/s)
    
    d1 = (np.log(s/k) + (r - q + (v**2)/2)*t) / (np.sqrt(t)*v)
    d2 = d1 - np.sqrt(t)*v
    
    p = k*np.exp(-r*t)*norm.cdf(-d2) - s*np.exp(-q*t)*norm.cdf(-d1)
    
    return p