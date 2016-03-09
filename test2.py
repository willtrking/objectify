# coding: utf-8

from bisect import bisect_left


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError
    
test = ((0,'hello'),(1,'world'),(2,'test'))

test= zip(*sorted(test,key=lambda t: t[1]))

test_idx = test[0]

test_keys = test[1]

del test

print test_idx
print test_keys

print index(test_keys,"world"), test_idx[index(test_keys,"world")]
print index(test_keys,"test"), test_idx[index(test_keys,"test")]
print index(test_keys,"hello"), test_idx[index(test_keys,"hello")]