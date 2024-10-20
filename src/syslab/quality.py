import math

def sigmoid(x):return 1/(1+math.exp(-max(-40,min(40,x))))
def train(rows,epochs=180):
    if not rows:raise ValueError('no training rows')
    w,b=0.,0.
    for _ in range(epochs):
        dw=db=0
        for x,y in rows:
            error=sigmoid(w*x+b)-y;dw+=error*x;db+=error
        w-=.1*dw/len(rows);b-=.1*db/len(rows)
    return {'weight':w,'bias':b}
def accuracy(model,rows):
    if not rows:raise ValueError('empty evaluation set')
    return sum((model['weight']*x+model['bias']>=0)==bool(y) for x,y in rows)/len(rows)
def valid_rows(rows):return [(x,y) for x,y in rows if isinstance(x,(int,float)) and math.isfinite(x) and y in (0,1)]
