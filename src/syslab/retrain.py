"""Isolated local retraining job; consumes JSON stdin, returns JSON stdout."""
import json,sys
from .quality import train,valid_rows

def main():
    data=json.load(sys.stdin);rows=valid_rows(data['rows'])
    if len(rows)<8:raise ValueError('insufficient clean training data')
    json.dump(train(rows),sys.stdout,allow_nan=False)
if __name__=='__main__':main()
