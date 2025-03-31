import numpy as np

# Edge Detection Metrics # images have 0 for black, 1 for white
def same_size(one,two): # Configure two matrices to the same siz e
    min_rows = min(one.shape[0], two.shape[0])
    min_cols = min(one.shape[1], two.shape[1])
    one = one[:min_rows, :min_cols]
    two = two[:min_rows, :min_cols]
    return one, two

def precision(tp, fp):
    if (tp + fp == 0): 
        return 0.0
    else:
        return tp/(tp+fp)
def recall(tp, fn):
    if (tp + fn == 0):
        return 0.0
    else: 
        return tp/(tp+fn)
def f1(p, r):
    if (p + r == 0): 
        return 0.0
    else: 
        return 2*((p*r)/(p+r))
def eda(tp, tn, fp, fn):
    if (tp +tn + fp + fn == 0):
        return 0.0
    else:
        return (tp+tn)/(tp+tn+fp+fn)
    
def metrics(ground, edge):
    ground, edge = same_size(ground, edge)
    tp = np.sum(np.logical_and(ground == 0, edge == 0))
    fp = np.sum(np.logical_and(ground == 255, edge == 0))
    tn = np.sum(np.logical_and(ground == 255, edge == 1))
    fn = np.sum(np.logical_and(ground == 0, edge == 1))
    p = precision(tp,fp)
    r = recall(tp, fn)
    print("precision:", p)
    print("recall:", r)
    print("f1:", f1(p,r))
    print("eda:", eda(tp, tn, fp, fn))