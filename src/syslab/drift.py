import math

def ks_statistic(a,b):
    if not a or not b:raise ValueError('two nonempty samples required')
    if any(not math.isfinite(v) for v in a+b):raise ValueError('nonfinite feature')
    a=sorted(a);b=sorted(b);i=j=0;maximum=0
    for value in sorted(set(a+b)):
        while i<len(a) and a[i]<=value:i+=1
        while j<len(b) and b[j]<=value:j+=1
        maximum=max(maximum,abs(i/len(a)-j/len(b)))
    return maximum

def threshold(n,m,alpha=.01):
    if n<1 or m<1 or not 0<alpha<1:raise ValueError('invalid sample or alpha')
    # Conservative asymptotic threshold, not an exact finite-sample p-value.
    return math.sqrt(-.5*math.log(alpha/2)*(n+m)/(n*m))
